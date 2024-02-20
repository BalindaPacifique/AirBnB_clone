<<<<<<< HEAD
#!/usr/bin/python3

=======
#!/usr/bin/env python
'''AirBNB console Classs'''
>>>>>>> efc09ee65dcf281eb950f09ca480871460d7992d
import cmd

class HBNBCommand(cmd.Cmd):
    """creating my own cmd interpreter"""
    prompt = "(hbnb)"
<<<<<<< HEAD
    
    def do_quit(self, line):
        """Quit command to exit the program"""
=======

    def do_quit(self, line):
        """exit the command line"""
>>>>>>> efc09ee65dcf281eb950f09ca480871460d7992d
        return True
    def do_EOF(self, line):
        """end the file"""
        return True
<<<<<<< HEAD
    def emptyline(self):
        """pass when recieving an empty line"""
        pass
=======
    def help_quit(self, line):
        """quit documentation"""
        print("Quit command to exit the program")
>>>>>>> efc09ee65dcf281eb950f09ca480871460d7992d
    def help(self, line):
        """Documented commands (type help <topic>):
           ========================================
               EOF  help  quit"""
    def default(self, line):
        """for unknown cmd"""
<<<<<<< HEAD
        print(f"Unkown commad:{line}")
    
=======
        print("Unkown commad:{}".format(line))

>>>>>>> efc09ee65dcf281eb950f09ca480871460d7992d
if __name__ == "__main__":
    HBNBCommand().cmdloop()
