import os
from os import stat
from pathlib import Path

if __name__ == "__main__":


    print(os.getcwd())
    with open(f"{Path.home()}/.bashrc", "a") as bashrc:
        bashrc.write("\n")
        bashrc.write(f"alias math='{os.getcwd()}/math.sh'")

    with open("math.sh", "w") as mathsh:
        run_string = f"""#!/bin/bash

source {os.getcwd()}/venv/bin/activate
str="$*"
python {os.getcwd()}/main.py $str
deactivate
"""
        mathsh.write(run_string)

    os.system("chmod +x math.sh")
    print("new status for math.sh", stat("math.sh"))

    print(f"run the following command to finish installation:  'source {Path.home()}/.bashrc'")