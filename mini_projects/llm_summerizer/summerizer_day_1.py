import argparse
import json
import os
import sys
import time
from datetime import datetime

import requests


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
MAX_ATTEMPTS = 3


def read_file(filename):
    with open(filename) as file:
        return file.read()
        

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
            print(f"Attempt {attempt} of {MAX_ATTEMPTS} failed.")
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


parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

try:
    text = read_file(args.filename)
    chunks = chunk(text)
    chunk_summaries = []
    for c in chunks:
        chunk_summaries = summarize(c)
    summary = "\n\n".join(chunk_summaries)
    output_file = save_json(args.filename, summary)
    print(f"Saved summary to {output_file}")
except FileNotFoundError:
    sys.exit(f"Error: file not found: {args.filename}")