# Entrypoint for grading
import os

USERNAME = "tronolllanj-creator"
# Gate: output must be 1-30 chars, one word, no trailing newline.
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
os.makedirs(out_dir, exist_ok=True)

if not (1 <= len(USERNAME) <= 30 and USERNAME.strip() and ' ' not in USERNAME):
    raise ValueError("Invalid username")

path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(USERNAME)

print(path)
print(len(USERNAME))
