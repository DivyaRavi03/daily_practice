import re
def count_levels(file):
    output = {}
    with open(file,'r') as f:
        text = f.read()
        lines = text.split('\n')
        for line in lines:
            m = re.match(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\s([A-Z]+)", line)
            if m:
                level = m.group(1)
                output[level] = 1 + output.get(level, 0)
    return output

with open("app.log", "w") as f:
    f.write("2026-11-11 10:00:01 INFO Server started\n")
    f.write("2026-11-11 10:00:05 WARNING Disk space at 85%\n")
    f.write("2026-11-11 10:01:12 ERROR Database connection failed\n")
    f.write("2026-11-11 10:01:15 INFO Retrying connection\n")
    f.write("this line is garbage\n")
    f.write("2026-11-11 10:01:20 ERROR Retry failed\n")
    f.write("\n")
    f.write("2026-11-11 10:02:00 INFO User ERROR-report downloaded\n")

with open("empty.log", "w") as f:
    f.write("")

assert count_levels("app.log") == {"INFO": 3, "WARNING": 1, "ERROR": 2}
assert count_levels("empty.log") == {}

print("All tests passed!")          