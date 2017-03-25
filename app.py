import config
from log import logger
from handle import exception_handler
from component import load_component
import sys
import os
from plugin import BasePlugin
import importlib.util
import threading
import traceback

class App:
      def __init__(self,logfilename,main_function,name="An Amazing app",init_function=None,on_exception=None):
          try: #here we'll initiallize app
            self.main_function=main_function
            self.plugins=dict()
            self.name=name
            self.threads=[]
            config.argv=sys.argv
            config.log=logger(logfilename)
            config.handler=exception_handler(on_exception,config.debug) #initiallized logger and exception handler
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
                   if(Plugin=="__pycache__" or Plugin=="__init__.py"):
                       continue
                   mod=importlib.util.spec_from_file_location(Plugin, config.plugins_folder+"/"+Plugin+"/main.py")#importing plugin
                   plg=importlib.util.module_from_spec(mod)
                   mod.loader.exec_module(plg)
                   _plg=plg.plugin(self)#calling on load function
                   _plg.on_load(self)
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
      def hw(self,i):
          print(str(i**2))
          self.plugins[0].run()
      def event(self,event):
          if event=="$APP_QUIT":
              config.log.log("Recieved quit signal.")
              config.run=False
          for plugin in self.plugins:
              config.log.log("Sending event to "+plugin)
              self.plugins[plugin].on_event(event)
              for component in self.plugins[plugin].components:
                  self.plugins[plugin].components[component].on_event(event)
      def run(self):#DONE:Add running main function
          config.log.log("Starting app")
          for plugin in self.plugins:
              plg=self.plugins[plugin]
              thrd=threading.Thread(target=config.handler.run_function,args=(plg.run,self,sys.argv,))
              self.threads.append(thrd)
              thrd.setDaemon(1)
          thrd=threading.Thread(target=config.handler.run_function,args=(self.main_function,self,))#adding main functiion to threading
          self.threads.append(thrd)
          thrd.setDaemon(1)
          for i in range(len(self.threads)):
              self.threads[i].start()
          for i in range(len(self.threads)):
              self.threads[i].join()
