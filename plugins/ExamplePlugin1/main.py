from plugin import BasePlugin#base class of plguin
import config
from event import Event
import time

class plugin(BasePlugin):#our own plugin
    name="Example2 1.0alpha"
    version="1.1.0alpha"
    author="(Unknown)"
    description="Example plugin"

    def on_load(self,app):
        self.add_component("ExampleComponent","exmpl1")#creating instance of component inside of our plugin
        self.components["exmpl1"].x=12#setting x of our component
        self.components["exmpl1"].add_component("ExampleSubComponent","exmpl2")

    def run(self,app,argv):
        while app.running:#
            time.sleep(10)
            #app.event(Event("10_SECONDS_PASSED",self,{"time":10}))
