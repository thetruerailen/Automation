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

Commands
```run_command(command)```: Executes the specified command and returns the output.

```print_command(message)```: Prints the specified message to the console.

```wait_command(seconds)```: Waits for the specified number of seconds.

```execute_command(cmd)```: Executes the specified command in the terminal.

```end_command()```: Signals the end of the script.

```input_command(prompt)```: Prompts the user for input and returns the input.

```if_command(condition, true_commands, false_commands)```: Evaluates a condition and executes the true commands if the condition is true, or the false commands if the condition is false.

```while_command(condition, commands)```: Executes a set of commands repeatedly while a condition is true.

```for_command(variable, iterable, commands)```: Executes a set of commands for each element in an iterable.

```function_command(name, arguments, commands)```: Defines a new function with the specified name, arguments, and commands.

```set_command(variable, value)```: Sets the value of a variable.

```read_command(filename)```: Reads the contents of a file and returns the contents as a string.

```write_command(filename, contents)```: Writes the specified contents to a file.

```import_command(module)```: Imports a module and makes its functions and variables available in the current scope.

```sleep_command(seconds)```: Pauses execution of the script for a specified amount of time.

```sqrt_command(x)```: Returns the square root of x.

```pow_command(x, y)```: Returns x raised to the power of y.

```sin_command(x)```: Returns the sine of x (in radians).

```cos_command(x)```: Returns the cosine of x (in radians).

```tan_command(x)```: Returns the tangent of x (in radians).

```atan_command(x)```: Returns the arctangent of x (in radians).

```rand_command()```: Returns a random float between 0 and 1.

```abs_command(x)```: Returns the absolute value of x.

```ceil_command(x)```: Returns the smallest integer greater than or equal to x.

```floor_command(x)```: Returns the largest integer less than or equal to x.

```round_command(x)```: Rounds x to the nearest integer.

```randint_command(a, b)```: Returns a random integer between a and b (inclusive).

```choice_command(seq)```: Returns a random element from the specified sequence.

```shuffle_command(seq)```: Shuffles the elements of the specified sequence.

```join_command(seq, delimiter)```: Joins the elements of the specified sequence into a string, separated by the specified delimiter.

```split_command(str, delimiter)```: Splits the specified string into a list of substrings, using the specified delimiter.

```strip_command(str, chars)```: Returns a copy of the specified string with leading and trailing characters removed.

```replace_command(str, old, new)```: Returns a copy of the specified string with all occurrences of the old substring replaced by the new substring.

```startswith_command(str, prefix)```: Returns True if the specified string starts with the specified prefix, False otherwise.

```endswith_command(str, suffix)```: Returns True if the specified string ends with the specified suffix, False otherwise.

```isalpha_command(str)```: Returns True if the specified string consists only of alphabetic characters, False otherwise.

```isdigit_command(str)```: Returns True if the specified string consists only of digits, False otherwise.

```islower_command(str)```: Returns True if all the alphabetic characters in the specified string are lowercase, False otherwise.

```isupper_command(str)```: Returns True if all the alphabetic characters in the specified string are uppercase, False otherwise.

```startswith_command(seq, item)```: Returns True if the specified sequence starts with the specified item, False otherwise.

```endswith_command(seq, item)```: Returns True if the specified sequence ends with the specified item, False otherwise.

```sum_command(seq)```: Returns the sum of all the elements in the specified sequence.

```min_command(seq)```: Returns the smallest element in the specified sequence.

```max_command(seq)```: Returns the largest element in the specified sequence.

```len_command(seq)```: Returns the length of the specified sequence.

```sorted_command(seq)```: Returns a new sorted list from the specified sequence.

```enumerate_command(seq)```: Returns an iterator that produces pairs of indices and elements from the specified sequence.

```zip_command(*seqs)```: Returns an iterator that aggregates elements from each of the specified sequences.

```any_command(seq)```: Returns True if any element in the specified sequence is True, False otherwise.

```all_command(seq)```: Returns True if all elements in the specified sequence are True, False otherwise.

```dir_command(obj)```: Returns a list of the attributes and methods of the specified object.

```getattr_command(obj, name)```: Returns the value of the specified attribute of the specified object.

```setattr_command(obj, name, value)```: Sets the value of the specified attribute of the specified object.

```hasattr_command(obj, name)```: Returns True if the specified object has the specified attribute, False otherwise.

```type_command(obj)```: Returns the type of the specified object.

```id_command(obj)```: Returns the unique identifier of the specified object.

```range_command(start, stop=None, step=None)```: Returns a sequence of numbers from start to stop, incremented by step (default is 1).

```filter_command(function, seq)```: Returns a new sequence consisting of the elements of the specified sequence for which the specified function returns True.

```map_command(function, seq)```: Applies the specified function to each element in the specified sequence and returns a new sequence with the results.

```reduce_command(function, seq)```: Applies the specified function to the first two elements in the specified sequence, then to the result and the next 
element, and so on, until a single value is returned.

```isinstance_command(obj, class_or_tuple)```: Returns True if the specified object is an instance of the specified class or tuple of classes, False otherwise.


## Usage
To execute a script, use the following command:

```
python script.py <script_file> end
```

The <script_file> parameter specifies the path to the script file. The end parameter is used to signal the end of the script.
