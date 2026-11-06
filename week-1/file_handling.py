import csv
import json
from pathlib import Path

data_dir = Path("week-1/data")
data_dir.mkdir(parents=True, exist_ok=True)

# Exercise: Write to and read from a text file
text_path = data_dir / "notes.txt"
text_path.write_text("I am learning Python for Machine Learning.\n", encoding="utf-8")
content = text_path.read_text(encoding="utf-8")
print("Text file content:", content)

# Exercise: Write and read CSV
students = [
    {"name": "Ram", "marks": 25},
    {"name": "Salina", "marks": 85},
    {"name": "Nishan", "marks": 92},
]
csv_path = data_dir / "students.csv"

with csv_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerows(students)

with csv_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("CSV records:")
    for row in reader:
        row["marks"] = int(row["marks"])
        print(row)

# Exercise: Write and read JSON
profile = {
    "name": "Nishan",
    "course": "Data Science",
    "skills": ["Python", "SQL", "Machine Learning"]
}
json_path = data_dir / "profile.json"

with json_path.open("w", encoding="utf-8") as file:
    json.dump(profile, file, indent=4)

with json_path.open("r", encoding="utf-8") as file:
    loaded_profile = json.load(file)

print("JSON profile:", loaded_profile)