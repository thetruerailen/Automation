import json
import sys
import subprocess
import time

def run_command(command):
    """
    Executes the specified command and returns the output.
    """
    return subprocess.check_output(command, shell=True)

def print_command(message):
    """
    Prints the specified message to the console.
    """
    print(message)

def wait_command(seconds):
    """
    Waits for the specified number of seconds.
    """
    time.sleep(seconds)

def execute_command(cmd):
    """
    Executes the specified command in the terminal.
    """
    run_command(cmd)

def end_command():
    """
    Signals the end of the script.
    """
    sys.exit(0)

def main():
    """
    Runs the script specified in the command-line argument.
    """
    if len(sys.argv) != 3 or sys.argv[2] != "end":
        print("Usage: python main.py <script> end")
        sys.exit(1)
    
    # Load the script from the file
    with open(sys.argv[1], "r") as f:
        script = json.load(f)
    
    # Execute each command in the script
    for command in script["commands"]:
        if command["type"] == "print":
            print_command(command["message"])
        elif command["type"] == "wait":
            wait_command(command["seconds"])
        elif command["type"] == "execute":
            execute_command(command["cmd"])
        elif command["type"] == "end":
            end_command()
        else:
            print("Error: Unknown command type")
            sys.exit(2)

if __name__ == "__main__":
    main()
