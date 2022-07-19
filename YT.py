import webbrowser
import time 
import os 
 
url = input("Enter Youtube URL:")
refreshpage = input("Enter refresh time in seconds:")
counter = input("How many views do you want? ")
 
def openURL():
    webbrowser.open(url)
    time.sleep(int(refreshpage))
    
    for i in range(int(counter)):
        print("Webpage has been viewed")
        openURL()
 
openURL()
