import plugin
import config
from plugin import BasePlugin
import datetime,time
from component import components
class plugin(BasePlugin):
    name="HelloWORLD V.I.P. edition"
    @classmethod
    def on_load(self,app):
        self.add_component(self,"HelloComponent","Hello1")
        config.log.log("I have being borned")
    def run(self,app,argv):
        config.log.log("OK"+str(argv))
        app.event("SOME_OTHER_EVENT")
        j=0
        while config.run:
            time.sleep(1)
            j=j+1
            config.log.log("This is plugin #0,j="+str(j))
            if(j>4):
                app.event("$APP_QUIT")
