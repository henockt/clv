"""
clv - visualize your command line scripts
henockt.github.io
"""
import sys, time

# draw x-mas tree
def tree(height, symbol="^"):
    """
    Given a height, outputs a tree of that height.

    height - integer - height of the tree

    OPTIONAL ARGUMENTS:
    -------------------
    symbol - string - '^' /caret/ by default, and is the tree symbol character
    """
    # check for erros
    if type(height) != int:
        raise RuntimeError("height can only be an int")
    if type(symbol) != str:
        raise RuntimeError("symbol can only be a str")
    if len(symbol) != 1:
        raise RuntimeError("symbol can only be a single char")

    # print tree
    for c in [*range(height)] + [int(height / 10)] * int((height / 4) + 1):
        print(f"{symbol * (c*2+1):^{height * 2}}")
    

# Countdown for closing the program
def cout(delay, text="Closing in: ", exit=True, exitvalue=0):
    """
    Given time in seconds, starts a countdown from delay.

    delay - integer - time in seconds before the program exits.

    OPTIONAL ARGUMENTS:
    -------------------
    text      - string  - "Closing in: " by default, and is the text right before the countdown.
    exit      - boolean - True by default, and specifies if the program is to be closed. 
    exitvalue - [args]  - 0 /success/ by default, and the value is passed to sys.exit().
    """
    # checks for errors in input
    if type(delay) != int:
        raise TypeError("delay can only be an int")
    if type(text) != str:
        raise TypeError("text can only be a str")
    if type(exit) != bool:
        raise TypeError("exit can only be a boolean")

    # closes showing a countdown from delay
    print(f"{text}", end="")
    writeToStdOut([str(i) for i in range(delay, 0, -1)], sdelay=1.0)
    if exit:
        sys.exit(exitvalue)

# Closes the program with no countdown
def out(delay, exitvalue=0):
    """
    Given time in seconds, closes the program after the given time.

    delay - integer - time in seconds before the program exits.

    OPTIONAL ARGUMENTS:
    -------------------
    exitvalue - [args] - 0 /success/ by default, and the value is passed to sys.exit().
    """
    # Checks for input errors
    if type(delay) != int:
        raise TypeError("delay can only be an int")
            
    # waits for delay and closes 
    time.sleep(delay)
    sys.exit(exitvalue)

# Prints a string
def writeToStdOut(strings, clear=1, delay=0.05, sdelay=1.0):
    """
    Given a string or list of strings, prints the string one by one clearing
    stdout for each string.

    strings - list/str - string to be written to stdout
    
    OPTIONAL ARGUMENTS:
    -------------------
    clear  - {0, 1} - 1 by default, and clears the stdout after finishing if set to 1
             and viceversa.
    delay  - float - 0.05 by default, and is the time difference between every
             character being written.
    sdelay - float - 1.0 by default, and is the time difference between every
             other string in a list.
    """
    # checks for input errors
    if (clear != 1) and (clear != 0):
        raise TypeError("clear can only be 0 or 1")
    if type(delay) != float:
        raise TypeError("delay can only be a float")
    if type(sdelay) != float:
        raise TypeError("sdelay can only be a float")

    if type(strings) == list:
        # Make sure every item is a string
        for item in strings:
            if type(item) != str:
                raise TypeError("can't iterate over a non-string data type")

        # iterate over and print
        for i in range(len(strings)):
            for j in strings[i]:
                sys.stdout.write(j)
                sys.stdout.flush()
                time.sleep(delay)

            # delay between every other string in the list    
            time.sleep(sdelay)

            # clears StdOut every other string in the list
            if ((i + 1) < len(strings)):
                sys.stdout.write("\b" * len(strings[i]))
                sys.stdout.write(" " * len(strings[i]))
                sys.stdout.write("\b" * len(strings[i]))

        # clear the last string in the list
        if (clear == 1):
            sys.stdout.write("\b" * len(strings[-1]))
            sys.stdout.write(" " * len(strings[-1]))
            sys.stdout.write("\b" * len(strings[-1]))

    elif type(strings) == str:
        for j in strings:
            sys.stdout.write(j)
            sys.stdout.flush()
            time.sleep(delay)
        
        # clear the string
        if (clear == 1):
            sys.stdout.write("\b" * len(strings))
            sys.stdout.write(" " * len(strings))
            sys.stdout.write("\b" * len(strings))