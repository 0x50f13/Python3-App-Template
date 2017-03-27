
class Event(object):
    def __init__(self,name,parent,data):
        """name--name of event
           parent--sender of event
           data--dict of information give about event"""
        self.name=name
        self.parent=parent
        self.data=data
    def __str__(self):
        return self.name
