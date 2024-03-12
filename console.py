#!/usr/bin/python3
"""
A console for our cli
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

current_classes = {'BaseModel': BaseModel, 'User': User,
                   'Amenity': Amenity, 'City': City, 'State': State,
                   'Place': Place, 'Review': Review}


def validated(arguments):
    """
    validates arguments during create
    """
    if len(arguments) != 1:
        print("** class name missing **")
        return False
    if arguments[0] not in current_classes:
        print("** class doesn't exist **")
        return False
    return True


def validated_up(arguments):
    """
    validates during show
    """
    if len(arguments) < 1:
        print("** class name missing **")
        return False
    if len(arguments) < 2:
        print("** instance id missing **")
        return False
    if arguments[0] not in current_classes:
        print("** class doesn't exist **")
        return False
    if len(arguments) < 3:
        print("** attribute name missing **")
        return False
    if len(arguments) < 4:
        print(" ** value missing **")
        return False
    return True


def validated_show(arguments):
    """
    validates during show
    """
    if len(arguments) < 1:
        print("** class name missing **")
        return False
    if len(arguments) < 2:
        print("** instance id missing **")
        return False
    if arguments[0] not in current_classes:
        print("** class doesn't exist **")
        return False
    return True


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
        """
        caters for empty line
        :return:
        """
        pass

    def do_create(self, line):
        """
        creates an argument
        """
        args = line.split()
        if not validated(args):
            return
        new = current_classes[args[0]]()
        new.save()
        print(new.id)

    def do_show(self, line):
        """
        Show an argument based on the id
        """
        args = line.split()
        if not validated_show(args):
            return
        instance = storage.all()
        key = f"{args[0]}.{args[1]}"
        requested = instance.get(key)
        if requested is None:
            print("** no instance found **")
            return
        print(requested)

    def do_destroy(self, line):
        """destroys an object"""
        args = line.split()
        if not validated_show(args):
            return
        instance = storage.all()
        key = f"{args[0]}.{args[1]}"
        requested = instance.get(key)
        if requested is None:
            print("** instance id missing **")
            return
        del instance[key]
        storage.save()

    def do_all(self, line):
        """
        prints all the objects in memory
        """
        args = line.split()
        instances = storage.all()
        if len(args) < 1:
            print(["{}".format(str(dicky)) for x, dicky in instances.items()])
            return
        if len(args) == 1:
            if args[0] not in current_classes.keys():
                print("** class doesn't exist **")
                return
            if args[0] in current_classes.keys():
                print(["{}".format(str(dicky))
                       for x, dicky in instances.items()
                       if args[0] == type(dicky).__name__])

    def do_update(self, line):
        """
        Updates the json
        usage "update <class name> <id> <attribute name> "<attribute value>
        """
        args = line.split()
        so_far = storage.all()
        if not validated_up(args):
            return
        key = f"{args[0]}.{args[1]}"
        if key not in so_far:
            print("** no instance found **")
            return
        to_update = so_far.get(key)
        if (args[3][0] == "\"") or (args[3][0] == "\'"):
            val = str(args[3])
        else:
            if "." in args[3]:
                val = float(args[3])
            else:
                val = int(args[3])
        a = to_update.to_dict()
        a[args[2]] = val
        ser_dict = {k: v.to_dict() for k, v in so_far.items()}
        ser_dict[key] = a
        with open("file.json", "w") as f:
            json.dump(ser_dict, f)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
