import json
def avg_latency_by_model(filename):
    output = {}
    skipped = 0
    with open(filename) as file:
        for line in file:
            if not line.strip():        # nothing on this line
                continue
            try: 
                data = json.loads(line)
                name = data["model"]
                ms = data["latency_ms"]
                if name not in output:
                    output[name] = [0,0]
                output[name][0]+=ms
                output[name][1] += 1
            except (json.JSONDecodeError, KeyError):
                skipped += 1
        final = {}
        for name, (total, n) in output.items():
            final[name] = round(total / n, 2)
            print(f"Skipped {skipped} bad lines")
        return final


with open("requests.jsonl", "w") as f:
    f.write('{"model": "gpt-4o", "latency_ms": 820, "status": 200}\n')
    f.write('{"model": "claude-sonnet", "latency_ms": 640, "status": 200}\n')
    f.write('{"model": "gpt-4o", "latency_ms": 1100, "status": 200}\n')
    f.write('\n')
    f.write('{"model": "claude-sonnet", "latency_ms": 710.5, "status": 200}\n')
    f.write('this is not json\n')
    f.write('{"model": "gpt-4o", "status": 500}\n')
    f.write('{"model": "llama-3", "latency_ms": 300, "status": 200}\n')

with open("empty.jsonl", "w") as f:
    f.write("")

assert avg_latency_by_model("requests.jsonl") == {
    "gpt-4o": 960.0,
    "claude-sonnet": 675.25,
    "llama-3": 300.0,
}
assert avg_latency_by_model("empty.jsonl") == {}

print("All tests passed!")


        
