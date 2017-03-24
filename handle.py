import datetime
import config

class exception_handler:
      def __init__(self,app,on_exception=None,show_trace=False):
        """Exception handler process exception if it occurs.
           on_exception(handler,exception,time)--function that process exceptions.
           exception--exception class
           handler-exception_handler
           time-time when exception occured
           show_trace--need to print trace or no"""
        self.app=app
        self.on_exception=on_exception
        self.show_trace=show_trace
      def exception(self,e):#exception function
         #self.on_exception(self,e,datetime.datetime.now())
         if(config.EXCEPTION_NOTIFY):
            self.app.event("$EXCEPTION")#"$" symbol before event meas that this internal app event
            config.logger.messagebox("Warning","An exception has occured!\n"+str(e))#showing text styled messagebox into log
            if(config.debug or self.show_trace):#if we need to show trace
               config.logger.write_stack()#writng trace
      def run_function(self,f,*args):#runs function with exception handling
          try:
              f(*args)#running given function with args
          except Exception as e:#if exception occurs
              self.exception(e)#processing it
