import subprocess


with open('extensions.txt','r') as f:
    lines = [line.split('\n')[0] for line in f.readlines()]
    for line in lines:
        subprocess.call(['code', '--install-extension', line])

print(lines)