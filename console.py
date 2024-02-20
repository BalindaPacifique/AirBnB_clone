#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """creating my own cmd interpreter"""
    prompt = "(hbnb)"
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    def do_EOF(self, line):
        """end the file"""
        return True
    def emptyline(self):
        """pass when recieving an empty line"""
        pass
    def help(self, line):
        """Documented commands (type help <topic>):
           ========================================
               EOF  help  quit"""
    def default(self, line):
        """for unknown cmd"""
        print(f"Unkown commad:{line}")
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
