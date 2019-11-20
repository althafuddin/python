import subprocess

proc = subprocess.run(["cat", "fake.txt"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(proc.stderr.decode())
