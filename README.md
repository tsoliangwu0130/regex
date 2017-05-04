Regex Note
==========

### Identifiers

| Identifiers | Meaning |
|-------------|---------|
| \  | escape character |
| \d | any number |
| \D | anything but a number |
| \s | space |
| \S | anything but a space |
| \w | any letter |
| \W | anything but a letter |
| \b | space around whole words |
| .  | any character, except for a new line |
| \. | period |

### Modifiers

| Modifiers | Meaning |
|-----------|---------|
| ? | match 0 or 1 |
| * | match 0 or more |
| + | match 1 or more|
| $ | match the end of a string |
| ^ | match the beginning of a string |
| &#124; | either or |
| [] | range or variance e.g. [A-Z]|
| {x}  | expecting x amount |
| {x, y} | expect to see this x-y amounts of the preceding code

### White Space Characters

| White Space Characters | Meaning |
|-----------|---------|
| \n | new line |
| \s | space |
| \t | tab |
| \e | escape |
| \f | form feed |
| \r | carriage return |

**_Note: Don't forget to escape the following characters if used!_**  
. + * ? [ ] $ ^ ( ) { } | \


### References

1. [Regular Expressions with re Python Tutorial](https://pythonprogramming.net/regular-expressions-regex-tutorial-python-3/)
