import config
from component import BaseCompoment

#Example of compnent
name="HelloComponent"
ALLOW_SUBCOMPONETNS=False #This means if this compnent couldn't have child components
class SubComponentsNotAllowed(Exception):#this exception will be raised if you'll try to add child component of component where 
    pass
class MainComponent(BaseCompoment):
    def __init__(self,parent,name,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs
        self.parent=parent
        self.name=name
        config.log.log("("+self.parent.name+"/"+self.name+"):Loading was ok.")
    def on_event(self,event):#replacing on_event function
        if event=="SAY_HELLO":#if event is SAY_HELLO then
            config.log.log("("+self.parent.name+"/"+self.name+"):Hello,everybody!!!There was an app event:"+event)#logging about parent of this component
