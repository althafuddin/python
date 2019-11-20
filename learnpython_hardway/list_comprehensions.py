import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name', help='name of the file')

args = parser.parse_args()

with open(args.file_name) as f:
    words = f.readlines()

new_words = [f"{w.strip()}-superhero" for w in words if w.startswith('D') in words]
# for w in words:
#     if w.startswith('Ant'):
#         new_words = f"{w.strip()}-superhero"
print(new_words)
