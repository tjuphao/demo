import re
import os

directory = r"C:\localProducts\GenVATC2X_Metro_VATO\GenVATC2X_Metro_VATO\implementation\ato_per"

# Match function definition: ends with ')' and does NOT end with ';', may have '{' or nothing after ')'
func_def_pattern = re.compile(
    r'^[\w\s\*\(\),]+\w+\s*\([^;]*\)\s*(\{)?\s*$'
)

for filename in os.listdir(directory):
    if filename.endswith('.c'):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()
        func_count = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            # Exclude prototypes (those ending with ';') and control statements and comment lines
            if (
                func_def_pattern.match(stripped)
                and not stripped.endswith(';')
                and not stripped.startswith('if')
                and not stripped.startswith('else if')
                and not stripped.startswith('switch')
                and not stripped.startswith('while')
                and not stripped.startswith('*')
            ):
                print(f"{stripped}, file: {filename}, line {i + 1}")
                func_count += 1
        print(f"Total functions identified in {filename}: {func_count}\n")