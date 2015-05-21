import subprocess
import os


for filename in os.listdir('data'):
    subprocess.check_output(["python", "script.py", "data/"+filename])
    print "Done file: " + filename


