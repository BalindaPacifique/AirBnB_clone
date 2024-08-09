#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    """
    This class is for the commanda line, which will allow
    our users to interact with the back end 
    """
    CLASSES = {
        "BaseModel": BaseModel()
    }
    prompt = "(hbnb)"
    def do_create(self, line):
        """ This module create a class"""
        args = line.split()
        class_name = args[0]
        self.CLASSES[class_name]
        storage.save()
        print(class_name.id)
        if not class_name:
            print("**class name missing**")
        else:
            print("**class name doesn't exist**")
    def do_show(self, line):
        """
        This module prints the string representation
        of an instance based on the class name and if
        """
        args = line.split()
        class_name = args[0]
        if not class_name:
            print("**class name missing**")
        elif not class_name.id:
            print("**instance id missing**")
        else:
            print("**class doesn't extist**")
    def do_destroy(self, line):
        """ Delete an instance based on class and id"""
        args = line.split()
        class_name = args[0]
        if not class_name:
            print("**class name missing**")
    def do_quit(self, line):
        """ Quit command to exit the program """
        return True
    def do_EOF(self):
        """ Ends the file"""
        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()
