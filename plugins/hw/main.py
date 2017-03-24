import plugin
import config
from plugin import BasePlugin
import datetime,time
from component import components
import sys
class plugin(BasePlugin):
    name="HelloWORLD Xclusive edition"
    @classmethod
    def on_load(self,app):
        self.add_component(self,"HelloComponent","Hello2")
        self.app=app
        config.log.log("I have being borned")
    def run(self,app,argv):
        app.event("SAY_HELLO")
        i=0
        while config.run:#plugin life cycle
            time.sleep(2)
            i=i+1
            config.log.log("This is plugin #1,i="+str(i)+",config.run="+str(config.run))
