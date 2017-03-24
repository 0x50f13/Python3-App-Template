import importlib.util
import config
class BaseCompoment(object):
    version="0.0.1alpha"
    author="Bob Smith"
    name="Abstarct1"
    description="Amazing component"
    def __init__(self,parent,name,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs
        self.parent=parent
        self.name=name
    def on_event(self,event):
        pass
components=dict()
def load_component(path,name):
    """loads compnent from specified path
       path--path to compnent"""
    mod=importlib.util.spec_from_file_location(name, path)#importing compnent
    component=importlib.util.module_from_spec(mod)
    mod.loader.exec_module(component)
    components[component.name]=component.MainComponent
    config.log.log(component.name+" loaded")#logging that new component succesfully loaded
