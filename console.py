#!/usr/bin/env python
'''AirBNB console Classs'''

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print("\nExiting the program.")
        return True

    def do_help(self, arg):
        """Show help message."""
        super().do_help(arg)

    def emptyline(self):
        """Do nothing on empty input line."""
        pass


if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
