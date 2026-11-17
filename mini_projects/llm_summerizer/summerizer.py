import argparse
import logging
import glob
import json
import os
import sys
import time
from datetime import datetime

import requests


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
MAX_ATTEMPTS = 3
CHUNK_SIZE = 2000


def reads_folder(path):
    if os.path.isdir(path):
        paths = sorted(glob.glob(os.path.join(path, "*.txt")))
        if len(paths) == 0:
            sys.exit(f"Error: no .txt files found in {path}")
    elif os.path.isfile(path):
        paths = [path]
    else:
        sys.exit(f"Error: path not found: {path}")
    return paths


def read_file(filename):
    with open(filename) as file:
        return file.read()


def chunk_text(text, size):
    chunks = []
    for i in range(0, len(text), size):
        chunks.append(text[i:i + size])
    return chunks


def summarize(text):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            reply = requests.post(
                OLLAMA_URL,
                json={
                    "model": OLLAMA_MODEL,
                    "prompt": "Summarize this text:\n\n" + text,
                    "stream": False,
                },
                timeout=60,
            )
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            logging.warning(f"Attempt {attempt} of {MAX_ATTEMPTS} failed.")
            if attempt < MAX_ATTEMPTS:
                time.sleep(2)
            continue

        data = reply.json()
        if reply.status_code != 200:
            # Errors like "model not found" won't fix themselves, so no retry
            sys.exit(f"Error from Ollama: {data.get('error')}")
        return data["response"]

    sys.exit("Error: could not reach Ollama. Is it running?")


def save_json(input_file, summary):
    output_file = os.path.splitext(input_file)[0] + ".json"
    result = {
        "input_file": input_file,
        "model": OLLAMA_MODEL,
        "created_at": datetime.now().isoformat(),
        "summary": summary,
    }
    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)
    return output_file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    try:
        list_paths = reads_folder(args.path)
        for path in list_paths:
            text = read_file(path)
            logging.info(f"Processing {path}")
            chunks = chunk_text(text, CHUNK_SIZE)
            chunk_summaries = []
            for i,c in enumerate(chunks):
                logging.info(f"Summarizing chunk {i+1}/{len(chunks)}")
                summ = summarize(c)
                chunk_summaries.append(summ)
            if len(chunk_summaries) > 1:
                logging.info(f"Combining {len(chunks)} chunk summaries")
                summary = "\n\n".join(chunk_summaries)
                summary = summarize(summary)
            else: 
                summary = chunk_summaries[0]
            output_file = save_json(path, summary)
            logging.info(f"Saved summary to {output_file}")
    except FileNotFoundError:
        sys.exit(f"Error: file not found: {args.path}")

if __name__ == "__main__":
    main()