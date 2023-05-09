#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass

    def create(self, arg):
        if arg is None:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_inst = BaseModel()
            new_inst.save()
            print(new_inst.id)
    
    def show(self, arg)
        if arg is None:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        elif    
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
