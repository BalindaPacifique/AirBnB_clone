#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """creating my own cmd interpreter"""
    prompt = "(hbnb)"
    
    def do_quit(self, line):
        """exit the command line"""
        return True
    def do_EOF(self, line):
        """end the file"""
        return True
    def help_quit(self, line):
        """quit documentation"""
        print("Quit command to exit the program")
    def help(self, line):
        """Documented commands (type help <topic>):
           ========================================
               EOF  help  quit"""
    def default(self, line):
        """for unknown cmd"""
        print(f"Unkown commad:{line}")
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
