import subprocess

cmd = 'git log --oneline -5'
output = subprocess.check_output(cmd, shell=True).splitlines()

# clean up
lines = [line.decode() for line in output]

# neat trick with print
print(*lines, sep='\n')
