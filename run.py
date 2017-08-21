from app import App as app
import time,datetime
import config
from event import Event
from job import job

MODULENAME="MAIN"
#Main file of our app
def custom_job(app,arg):
    i=0
    while app.running:
          config.log.log(str(i))
          i=i+1
          if(i>5):
              break
          time.sleep(5)
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
   App=app("app.log",main,[job(custom_job,(10,))])#creating app
   App.run()#and running it
