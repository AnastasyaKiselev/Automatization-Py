class User:
    fname = ''
    last_name = ''
    def __init__(self, first_name, last_name):
        print ("Hello")
        self.fname=first_name
        self.lname = last_name

    def firstName(self):
        print(self.fname)

    def lastName(self):
        print(self.lname)    

    def bothName(self):
        print(self.fname + " " + self.lname)

    
