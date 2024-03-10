#!/usr/bin/python3
import cmd
"""
A console for our cli
"""

class HBNBCommand(cmd.Cmd):
    """
    A class for our console
    """
    prompt = '(hbnb) '
    def do_EOF(self, line):
        """
        instruction for end of file
        """
        return True

    def do_quit(self, line):
        """
        quit the console
        """
        return True

    def emptyline(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
