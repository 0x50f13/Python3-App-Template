from component import components
import multiprocessing
import config
import sys
class BasePlugin(object):
      name="Abstarct plugin"
      version="0.0.1alpha"
      author="Bob Smith"
      description="HelloWORLD plugin"
      components=dict()
      def __init__(self,app,*args,**kwargs):
          self.parent=app
          self.kwargs=kwargs
          self.args=args
      def __call__(self):
          self.run(self.parent,[])
      def add_component(self,__component,name,*args,**kwargs):
          """adds compnent to plugin
             __component--component class
             name--new unique name of component"""
          _component=components[__component](self,name)
          self.components.update({name:_component})
      @staticmethod
      def run(self,app,argv,*args,**kwargs):
          pass
      @classmethod
      def on_exception(self,e):#e is exception class
          pass
      @classmethod
      def on_load(self,app):
          pass
      @classmethod
      def on_event(self,event):
          config.log.log("(PLUGINS/%s):"%self.name+" recived event:"+event)
      @classmethod
      def on_cmd(self,cmd,args):
          pass
