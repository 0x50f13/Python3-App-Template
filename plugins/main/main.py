import plugin
import config
from plugin import BasePlugin
import datetime,time
from component import components
class plugin(BasePlugin):#our plugin
    name="HelloWORLD V.I.P. edition"#name of it
    @classmethod
    def on_load(self,app):#when plugin is initiallized(usually in App.__init__ function)
        self.add_component(self,"HelloComponent","Hello1")#adding component
    def on_event(self,event):#custom event procedding
        print("I recieved something very important:"+event)
    def run(self,app,argv):#called when app runs
        #config.log.log("OK"+str(argv)) neded for debug
        app.event("SOME_OTHER_EVENT")#broadcasting event
        j=0#counnter of cycles
        while self.parent.running:
            time.sleep(1)#illusion of doing smth
            j=j+1#incresing counter
            config.log.log("This is plugin #0,j="+str(j))#logging some debug info
            if(j>4):#if counter is bigger then four
                app.event("$APP_QUIT")#asking the whole app to stop
