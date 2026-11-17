# LLM Text Summarizer (CLI)

A command-line tool that summarizes `.txt` files with a local LLM through [Ollama](https://ollama.com) and saves each summary as JSON.

It works on a single file or a whole folder, handles long documents by splitting them into chunks (map-reduce summarization), and retries automatically when the LLM server is unreachable.

## Features

- **File or folder input:** summarize one `.txt` file or every `.txt` file in a folder
- **Long-text chunking:** splits text into chunks, summarizes each one, then combines them into one final summary
- **Retry on failure:** up to 3 attempts, 2 seconds apart, when Ollama can't be reached or times out
- **Clear error handling:** missing files, empty folders, empty files, unknown models and a stopped server all give readable messages instead of tracebacks
- **Configurable through environment variables:** no settings hardcoded in the code
- **Logging:** timestamped progress messages with levels (INFO / WARNING)
- **Tested:** pytest tests with the LLM call mocked, so they run without Ollama

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running locally

## Setup

1. **Install Ollama and pull a model**

   ```bash
   ollama pull llama3.2:3b
   ```

2. **Clone the repo and create a virtual environment**

   ```bash
   git clone <your-repo-url>
   cd llm_summerizer
   python3 -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Summarize a single file:

```bash
python summerizer.py sample.txt
```

Summarize every `.txt` file in a folder:

```bash
python summerizer.py docs/
```

Each summary is saved next to its input file with the same name: `docs/notes.txt` → `docs/notes.json`.

Example output:

```
2026-11-17 14:55:49,895 INFO Processing docs/long.txt (2 chunks)
2026-11-17 14:55:49,895 INFO Summarizing chunk 1/2
2026-11-17 14:56:01,368 INFO Summarizing chunk 2/2
2026-11-17 14:56:04,561 INFO Combining 2 chunk summaries
2026-11-17 14:56:10,488 INFO Saved summary to docs/long.json
```

### Output format

```json
{
  "input_file": "docs/long.txt",
  "model": "llama3.2:3b",
  "created_at": "2026-11-17T14:56:10.488021",
  "summary": "The text discusses..."
}
```

## Configuration

Settings are read from environment variables, with defaults:

| Variable | Default | Description |
|---|---|---|
| `OLLAMA_URL` | `http://localhost:11434/api/generate` | Ollama API endpoint |
| `OLLAMA_MODEL` | `llama3.2:3b` | Model used for summarizing |

Example: use a different model:

```bash
export OLLAMA_MODEL=qwen2.5:3b
python summerizer.py docs/
```

## How it works

1. **Find files:** a folder path is expanded to its `.txt` files; a file path becomes a one-item list.
2. **Chunk:** each file's text is split into 2,000-character chunks so it fits in the model's context window. Small models silently cut off input that's too long.
3. **Map:** each chunk is summarized separately.
4. **Reduce:** if there was more than one chunk, the chunk summaries are summarized again into one final summary.
5. **Save:** the result is written to a JSON file next to the input.

### Error handling

| Situation | Behavior |
|---|---|
| Path doesn't exist | Exits with `Error: path not found` |
| Folder has no `.txt` files | Exits with `Error: no .txt files found` |
| File is empty | Logs a warning and skips it |
| Ollama not running / timeout | Retries up to 3 times, then exits with a clear error |
| Model not found (HTTP 404) | Exits immediately; retrying can't fix a client error |

## Running tests

```bash
python -m pytest
```

The tests mock `requests.post`, so they run without Ollama:

- `test_chunk_text`: chunking of normal, short and empty text
- `test_summarize`: returns the model's response from a successful API call
- `test_retry`: a failed connection is retried and the second attempt succeeds

## Project structure

```
llm_summerizer/
├── summerizer.py         # CLI tool
├── test_summerizer.py    # pytest tests
├── requirements.txt
└── README.md
```
