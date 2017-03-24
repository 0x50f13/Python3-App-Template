from app import App as app
import time

def main(app):
    while True:
        time.sleep(2)
        print("Hello!")

if __name__=="__main__":
   App=app("app.log",main)
   App.run()
