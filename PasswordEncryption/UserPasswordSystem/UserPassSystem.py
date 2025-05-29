##this is a python program which will act as a password system using a hashmap

class passwordSystem:
    def __init__(self):
        self.data = {}  #using self here in the init will persistently store user credentials
    
    def mapCreate(self, username, password):
        self.data[username] = password
        
    def checkLogin(self, username, password):
        return username in self.data and self.data[username] == password    #returns true or false 
             # ^check key in data         ^check value attatched to key 
class userMenu:
    def __init__(self):
        self.obj = passwordSystem() #constructor method, instantiates passwordSysten
    
    def menu(self):
        setFlag = '0' #flag for resetting user/pass prompt
        while(1):
            if setFlag == '0':
                choice = input("Create Account(1) or Login(2)?\n")
            if choice == '1':
                username = input("Create a Username: ")
                password = input("Create a assword: ")
                self.obj.mapCreate(username, password)
                print(f"{username}'s account created")
                
            elif choice == '2' or setFlag == '1':
                userCheck = input("Enter your Username: ")
                passCheck = input("Enter your password: ")
                if self.obj.checkLogin(userCheck, passCheck):
                    print("Access Granted")
                    setFlag = '0'
                else:
                    print("Incorrect username or password")
                    setFlag = '1'
            elif choice == 3:
                print("Exiting...")
                break
            else:
                print("Invalid Menu Selection")

#run system
obj1 = userMenu()
obj1.menu()
