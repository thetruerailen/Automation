# Documentation

## Description

This is a simple scripting language designed for automation purposes. The language is designed to be simple and easy to use, with commands specified in a JSON file. The language supports basic commands such as printing messages, waiting for a specified amount of time, executing commands on the terminal, and signaling the end of the script.

## Syntax
The syntax of the language is specified in a JSON file. The file consists of a list of commands, each command consisting of a type and any additional parameters required by the command. Here is an example of the syntax:

```json
{
  "commands": [
    {
      "type": "print",
      "message": "Hello, world!"
    },
    {
      "type": "wait",
      "seconds": 5
    },
    {
      "type": "execute",
      "cmd": "echo 'Script completed.'"
    },
    {
      "type": "end"
    }
  ]
}
```

## Commands
1. print: Prints a message to the console. The message parameter specifies the message to be printed.
2. wait: Waits for a specified amount of time. The seconds parameter specifies the number of seconds to wait.
3. execute: Executes a command on the terminal. The cmd parameter specifies the command to be executed.
4. end: Signals the end of the script. This command does not take any parameters.

## Usage
To execute a script, use the following command:

```
python script.py <script_file> end
```

The <script_file> parameter specifies the path to the script file. The end parameter is used to signal the end of the script.
