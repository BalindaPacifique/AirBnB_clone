#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """
    This class is for the commanda line, which will allow
    our users to interact with the back end 
    """
    def do_quit(self, line):
        """ This module quits the command line"""
        return True
    def do_EOF(self):
        """ Ends the file"""
        return True
if __name__ == "__main__":

    
    HBNBCommand().cmdloop()