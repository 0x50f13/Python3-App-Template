import inspect
import datetime
import config

LEVEL_ERROR = 0
LEVEL_WARN = 1
LEVEL_INFO = 2

LEVEL_TO_STR = ["E", "W", "I"]


class logger:
    def __init__(self, filename="app.log", verbose=2, template="{time}:{lvl}/{module}:{msg}", use_color=False):
        """filename--log filename
           verbose--verboseness of output
               default:2
               verbose=0 -- errors only
               verbose=1 -- errors+warns
               verbose>1 -- all
            template -- string template in python format
               default:'{time}:{lvl}/{module}:{msg}'
               time-time of message
               lvl-level of message(Error,info,warn)
               module -- module that has sent message
               msg-message itself
            use_color -- make messages colored in console or not
          """
        self.logfile = open(filename, "w+")  # open logfile
        self.logfile.write("Log started at " + str(datetime.datetime.now()) + "\n")  # logs when logging started
        self.template = template
        self.verbose = verbose
        self.use_color = use_color

    def log(self, msg, lvl=2, modulename=None, custom_template=None):
        """msg--log message string
           lvl--message level(Error,Warning,Info)"""
        color = ""
        color_end = ""
        if modulename is None:
            # TODO:GET IT AUTOMATICALLY
            modulename = "???"
        template = self.template
        if custom_template is not None:
            template = custom_template
        if config.debug:
            if self.verbose <= lvl:
                print( template.format(time=str(datetime.datetime.now()), lvl=LEVEL_TO_STR[lvl], module=modulename, msg=msg))
        self.logfile.write(template.format(time=str(datetime.datetime.now()), lvl=LEVEL_TO_STR[lvl], module=modulename,msg=msg))  # write message to log with date time

    def write_stack(self):
        """wrtie full call stack"""
        stack = inspect.stack()  # getting stack
        self.logfile.write("<STACK>:")
        for call in stack:  # processing each call
            self.logfile.write(str(call))

    def messagebox(self, title, msg, lvl, modulename=None, _file=""):
        """write to log text styled messagebox
             title--title for messagebox
             msg--message inside the messagebox
             file where -from where it was called"""
        box = "\n"  # Fixing Issue #5
        box = box + "+-------|%s" % title + "\n"  # writing messagebox header
        for line in msg.split("\n"):
            box = box + "|" + line + "\n"
        box = box + "|at " + _file + "\n"
        box = box + "+-------" + "-" * len(title)
        self.log(box, lvl, modulename)
