import inspect
import datetime
import config
class logger:
      def __init__(self,filename):
          """filename--log filename"""
          self.logfile=open(filename,"w+") #open logfile
          self.logfile.write("Log started at "+str(datetime.datetime.now())+"\n")#logs when logging started
      def log(self,msg):
          """msg--log message string"""
          if config.debug:
              print("["+str(datetime.datetime.now())+"]:"+msg)
          self.logfile.write("["+str(datetime.datetime.now())+"]:"+msg+"\n") #write message to log with date time
      def write_stack(self):
          """wrtie full call stack"""
          stack=inspect.stack() #getting stack
          self.logfile.write("<STACK>:")
          for call in stack: #processing each call
              self.logfile.write(str(call))
      def messagebox(self,title,msg,trace_lvl=3,auto_lvl=True):
          """write to log text styled messagebox
             title--title for messagebox
             msg--message inside the messagebox
             trace_lvl--how many levels we need get into stack"""
          self.log("")
          stack=inspect.stack()
          if auto_lvl:
              trace_lvl=len(stack)-1
          self.log("+-------|%s"%title) #writing messagebox header
          for line in msg.split("\n"):
               self.log("|"+line)
          self.log("|at "+str(stack[trace_lvl][1])+":"+str(stack[trace_lvl][2])+"("+str(stack[trace_lvl][3])+")")
          self.log("+-------"+"-"*len(title))
