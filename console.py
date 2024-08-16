#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import shlex

class HBNBCommand(cmd.Cmd):
    """
    This class is for the commanda line, which will allow
    our users to interact with the back end 
    """
    CLASSES = {
        "BaseModel": BaseModel,
        "User" : User
    }
    prompt = "(hbnb)"
    def do_create(self, line):
        """ This module create a class"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        This module prints the string representation
        of an instance based on the class name and if
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """ Delete an instance based on class and id"""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.CLASSES:
            print("** instance id missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], ars[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """ 
        Prints all string representation of all 
        instances based or not on the class name
        """
        args = shlex.split(line)
        objects = storage.all()

        if len(args) == 0:
            for key, values in objects.items():
                print(str(values))
        elif args[0] not in objects:
            print("** class doesn't exist**")
        else:
            for key, values in objects.items():
                if key.split(".")[0] == args[0]:
                    print(str(values))

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        pass

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True
    def do_EOF(self):
        """ Ends the file"""
        return True
if __name__ == "__main__":
    HBNBCommand().cmdloop()
