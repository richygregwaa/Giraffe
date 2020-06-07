from Chef27 import Chef

class ChineseChef(Chef):

    def make_special_dish(self):
        print("The chef makes orange chicken")  # this will override what was inherited from Chef

    def make_fried_rice(self): # this is additional to what was inherited from Chef
        print("The chef makes fried rice")