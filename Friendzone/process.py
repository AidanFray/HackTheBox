import subprocess
import time


"""
    Python script that is used to check for periodical
    task being run in the background
"""

def get_proc():
    return subprocess.check_output(["ps", "aux"]).decode("utf-8")

def diff(newState, oldState):

    oldLines = oldState.split("\n")
    newLines = newState.split("\n")

    for n in newLines:
        if not n in oldLines:

            # Removes process this script creates
            if not "process.py" in n:
                if not "ps aux" in n:
                    print(n, flush=True)

inital_state = get_proc()

while(True):
    state = get_proc()
    diff(state, inital_state)
    time.sleep(1)