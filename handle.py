import datetime
import config
import sys,os
import inspect

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
      def exception(self,e,_file=""):#exception function
         #self.on_exception(self,e,datetime.datetime.now())
         if(config.EXCEPTION_NOTIFY):
            #self.app.event("$EXCEPTION")#"$" symbol before event meas that this internal app event
            config.log.messagebox("Warning","An exception has occured!\n"+str(e)+"\n",_file)#showing text styled messagebox into log
            if(config.debug or self.show_trace):#if we need to show trace
               config.log.write_stack()#writng trace
      def run_function(self,f,*args):#runs function with exception handling
          try:
              f(*args)#running given function with args
          except Exception as e:#if exception occurs
              #print("EXCEPTION:"+str(e))
              exc_type, exc_obj, exc_tb = sys.exc_info()
              fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
              if self.on_exception != None:
                  self.on_exception(e)
              self.exception(e,inspect.getfile(f)+":"+str(inspect.getsourcelines(f)[-1]))#processing it
              if config.CRASH_ON_EXCEPTIONS:
                  config.log.log("Application crashing!!!\nCRASH_ON_EXCEPTIONS=True\nSending $APP_QUIT")
                  self.app.event("$APP_QUIT")
