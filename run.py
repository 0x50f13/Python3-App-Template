from app import App as app
import time
import config
#This app not fully ended!!!

#Main file of our app
def main(app):#main function
    while config.run:#!!!IMPORTANT!!!:life cycle should continue only while app running,otherwise app will run forever!
        time.sleep(3)#just doing smth
        print("This is main function")

if __name__=="__main__":#if we're running not as module
   App=app("app.log",main)#creating app
   App.run()#and running it
