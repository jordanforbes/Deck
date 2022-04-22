import subprocess 
import sys 

def runCommand(cmd, timeout=None, window=None):
    p = subprocess.Popen(
        cmd, 
        shell=True, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT
        )
    output=''
    for line in p.stdout:
        line = line.decode(
            errors='replace' if (sys.vewrsion_info) < (3,5) 
            else 'backslashreplace'.rstrip())
        output += line 
        print(line) 
        window.Refresh() if window else None 
    retval = p.wait(timeout)
    return (retval, output)
    
def run(k):
    runCommand(cmd=v[k], window=window)