#This is example component

from component import BaseCompoment#base class of component
import config

name="ExampleComponent"

class MainComponent(BaseCompoment):#IMPORTANT:class of your component shold be name MainComponent,if it named
      author="(Unknown)"#your name here
      version="1.1.0pre-release"#version of compnent
      ALLOW_SUBCOMPONETNS=True#allow subcomponent(component that have this component as parent)
      x=0
      def on_event(self,event):
          config.log.log("(%s/%s)"%(self.parent.name,self.name))
          if event.name=="UI_COMMAND_SENT":#user entered something to UI(this is main function)
              if event.data["cmd"]=="example":#if user input was example
                 config.log.log("I am an example compoenet.Here data about me:\nName:"+self.name+"Subcomponents:"+str(self.subcomponents)+"\nName of my parent:"+self.parent.name+"\nParent class:"+str(self.parent)+"\nx=%d"%self.x+"\n")#printing information about our component
