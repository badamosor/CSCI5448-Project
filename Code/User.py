import DBQuery
import Playlist

class User ():
 
    password = ""
    email = ""
    collaborating = []
    playlists = []

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    
if __name__ == '__main__':

    myUser = User()

### Set and get Password 
    myUser.setPassword("123")
    print ("password: " +  myUser.getPassword())

### Set and get Email 
    myUser.setEmail("abc@example.com")
    print ("Email: " +  myUser.getEmail())
