import csv
def column_average(filename, column):
    with open(filename) as f:
        sum = 0
        total = 0
        position = None
        file = csv.reader(f)
        header = next(file)
        for i in range(len(header)):
            if header[i] == column:
                position = i
        for row in file:
            if row[position] == '':
                continue
            sum += float(row[position])
            total +=1

        if total == 0:
            return None
        return sum/total
        



with open("students.csv", "w") as f:
    f.write("name,age,score,notes\n")
    f.write("Asha,22,80,\n")
    f.write("Ben,25,90,\n")
    f.write("Chen,23,,\n")
    f.write("Dina,24,70,\n")

with open("header_only.csv", "w") as f:
    f.write("name,age\n")

assert column_average("students.csv", "age") == 23.5
assert column_average("students.csv", "score") == 80.0
assert column_average("students.csv", "notes") is None
assert column_average("header_only.csv", "age") is None

print("All tests passed!")