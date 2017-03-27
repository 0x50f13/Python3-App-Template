import config
from log import logger
from handle import exception_handler
from component import load_component,components
import sys
import os
from plugin import BasePlugin
import importlib.util
import threading
import traceback
from event import Event

class App:
      def __init__(self,logfilename,main_function,version="1.0.0.0beta",name="An Amazing app",init_function=None,on_exception=None):
          try: #here we'll initiallize app
            self.main_function=main_function
            self.plugins=dict()
            self.name=name
            self.components=dict()#IMPORTANT:This is not componets that are loaded,but components of app(NOT plugins!)
            self.threads=[]
            self.running=True
            config.argv=sys.argv
            config.log=logger(logfilename)
            config.handler=exception_handler(self,on_exception,config.debug) #initiallized logger and exception handler
            #here we will load app components
            config.log.log("Loading components:")
            _components=os.listdir(config.components_folder)
            sys.path.insert(0,config.components_folder)
            for component in _components:
                if(component=="__init__.py" or component=="__pycache__"):
                    continue
                load_component(config.components_folder+"/"+component+"/main.py",component)
            config.log.log("Loading plugins:")
            _plugins=os.listdir(config.plugins_folder)#get list of all available plugins
            sys.path.insert(0, config.plugins_folder)
            for Plugin in _plugins:
                try:
                   if(Plugin=="__pycache__" or Plugin=="__init__.py" or not os.path.isfile(config.plugins_folder+"/"+Plugin+"/main.py")):
                       continue
                   mod=importlib.util.spec_from_file_location(Plugin, config.plugins_folder+"/"+Plugin+"/main.py")#importing plugin
                   plg=importlib.util.module_from_spec(mod)
                   mod.loader.exec_module(plg)
                   _plg=plg.plugin(self)
                   _plg.on_load(self)#calling on load function
                   self.plugins.update({_plg.name:_plg})
                   config.log.log(plg.plugin.name+" loaded")#logging that new plguin succesfully loaded
                except Exception as e:
                   config.log.log("Couldn't load plugin:"+Plugin+"\nException:"+str(e))#logging about exception while loading plugin
                   if(config.debug):
                       traceback.print_exc(file=sys.stdout)
                   config.log.messagebox("Warning","Could not load plugin:"+Plugin)
            if init_function!=None:#if we're given init function
                init_function(self)#run it
          except Exception as e:
            print("An a fatal exception occured during regestring app main class:"+str(e))
            if(config.debug):
                traceback.print_exc(file=sys.stdout)
            print("This application has crashed.")
            sys.exit(-1)
      def add_component(self,component,name):
          _component=components[component](self,name)
          self.components.update({name:_component})
      def event(self,event):
          if config.SHOW_EVENTS_IN_LOG:
             config.log.log("EVENT:\n"+"Name:%s\nParent:"%event.name+event.parent.name)

          if event.name=="$APP_QUIT":#FIXME:Issue #1:Plugins work after $APP_QUIT event
              config.log.log("Recieved quit signal.")
              self.running=False

          for component in self.components:
              self.components[component].on_event(event)#FIXED:Issue #3:App components do not recieve events
              for _component in self.components[component].subcomponents:
                  self.components[component].subcomponents[_component].on_event(event)
          for plugin in self.plugins:
              config.log.log("Sending event to "+plugin)
              self.plugins[plugin].on_event(event)
              for component in self.plugins[plugin].components:
                  self.plugins[plugin].components[component].on_event(event)
      def run(self):#DONE:Add running main function
          config.log.log("Starting app")
          #self.add_component("HelloComponent","Hello1")
          for plugin in self.plugins:
              plg=self.plugins[plugin]
              thrd=threading.Thread(target=config.handler.run_function,args=(plg.run,self,sys.argv,))
              self.threads.append(thrd)
              thrd.setDaemon(1)
          if self.main_function!=None:
              thrd=threading.Thread(target=config.handler.run_function,args=(self.main_function,self,))#adding main functiion to threading
              self.threads.append(thrd)
              thrd.setDaemon(1)
          for i in range(len(self.threads)):
              self.threads[i].start()
          for i in range(len(self.threads)):
              self.threads[i].join()
