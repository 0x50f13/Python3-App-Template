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
      def add_component(self,__component,name,*args,**kwargs):
          """adds component to plugin
             __component--component name from components
             name--new unique name of component"""
          _component=components[__component](self,name,*args,**kwargs)
          self.components.update({name:_component})
          self.components[name].on_create()
      @staticmethod
      def run(self,app,argv,*args,**kwargs):
          pass
      @classmethod
      def on_load(self,app):
          pass
      @classmethod
      def on_event(self,event):
          config.log.log("(PLUGINS/%s):"%self.name+" recived event:"+str(event))
