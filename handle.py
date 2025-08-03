import chardet
import json

# Step 2: Detect file encoding
with open('db_backup.json', 'rb') as file:
    result = chardet.detect(file.read())
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")

# Step 3: Load file with correct encoding and optionally re-encode to UTF-8
with open('db_backup.json', 'r', encoding=encoding) as file:
    data = json.load(file)

# Optionally save the data in utf-8 encoding
with open('db_backup_utf8.json', 'w', encoding='utf-8') as file:
    json.dump(data, file)