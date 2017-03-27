from app import App as app
import time
import config
from event import Event

#Main file of our app
def main(app):#main function
    while app.running:#!!!IMPORTANT!!!:life cycle should continue only while app running,otherwise app will run forever!
          s=input(">")
          if s=="help":
              print("example--example showcase\nexit--quit app\nhelp--shiw this message")
          if s=="exit":
              app.event(Event("$APP_QUIT",app,{"reason":"user_exit"}))
          else:
              app.event(Event("UI_COMMAND_SENT",app,{"cmd":s}))

if __name__=="__main__":#if we're running not as module
   App=app("app.log",main)#creating app
   App.run()#and running it
