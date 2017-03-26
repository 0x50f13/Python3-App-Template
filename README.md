# Python3AppTemplate
<p>
App template with plugins for python 3. <b>Beta-version</b>
</p>
<p>
<b>License:</b>GNU/GPL v3.0
</p>
# Description(tiny):
<p>
This app is fully extendable and allows to use components and plugins.<br>
*<b>Component is that part of app that could be used as well by app and plugins(e.g. button)</b><br>
All plugins are work in multithreading and could use all of app parts,such as logging,exception handling and others.

# Usage

The simpiest way is to create main function and start app with it.<br>
So main class of this template is App<br>
To initiallize it you need:<br>
<b>logfilename</b>--name of file where log will be stored<br>
<b>main_function</b>--function that will be runned with app,called with params:parent(app class)<br>
Non-required params:<br>
<b>init_function</b>--function called after all app initiallized(params same with main_function)<br>
<b>on_exception</b>--function called if exception occurs(params e-- Exception class)
Example:
```python
from App import App
import config
import time #We need sleep from here

def main(parent): #main function will be runned with app as parent of
    config.log.log("Hello,World!!!") #logging message to logfile
    cycles=0 #counter of cycles(after 5 we'll stop)
    while parent.running:
          cycles=cycles+1
          time.sleep(1) #pretending that we're doing something important
          if cycles>5: #we're done with our task,so
             parent.event("$APP_QUIT")#quitting app you could also try using parent.running=False(but I didn't check,and if you're using plugins it is strongly unrecommended.

if __name__=="__main__":
   app=App("app.log",main_function,"Example1") #creating our app
   app.run()#and running it
```    
