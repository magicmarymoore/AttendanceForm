#IMPORTS
import requests #to submit the form
import schedule #to have it submit the form on the correct days
import time #to have a little break
from twilio.rest import Client

#VARIABLES
url = 'https://docs.google.com/forms/d/e/1FAIpQLSfOUoMzCNO03o9ZmCa3zFYlZhdzWpGs9Y_6nSmcv-6kDlbdMg/formResponse' #url of google form to be filled out -- not actual url, this is just a placeholder
finalData = [] #list that will eventually hold all data to be submitted
#values ot be submitted
lastname = 'Moore'
firstname = 'Mary'
inschool = 'Yes'

values = { #"entry.number": value --> each question on the form has it's own unique id, to find the id right click + inspect element on the form or cmd+option+u
            # last name
            "entry.1134419109": lastname,
            # first name
            "entry.1339207634": firstname,
            # attending classes??
            "entry.1110466512": inschool,
        }
finalData.append(values) #add the data to the list

#client in order to send confirmation text
#set up using twilio (https://www.twilio.com/) --> Client(account SID, auth token)
client = Client("AC50d889a7d2c262e728951e29cda0bdb7", "30bbb5bc5d7e117ef93a9ee87e286bb1")

#function to submit the form
def sendAttendance(url, data):
    for d in data:
        try:
            requests.post(url, data=d) #subit the form
            print("form submitted")
            #to: your phone #, from: twilio acct. phone # (both these #s are currently placeholders...)
            client.messages.create(to="+12189632681", from_="+12345678901", body="form submitted")
        except:
            print("error!")
            client.messages.create(to="+12189632681", from_="+12345678901", body="error!")

#sendAttendance(url, finalData)

def workpls(): #b/c the schedule thing was weird and couldn't run a function w/params or smth...
    sendAttendance(url, finalData)

#only need to fill out the form on mon-wed (in-school thurs-fri)
#fill it out at 8:00 AM
schedule.every().monday.at("08:00").do(workpls)
schedule.every().tuesday.at("08:00").do(workpls)
schedule.every().wednesday.at("08:00").do(workpls)

while True: #do the things, all the time --> this is probably overkill, there is most definately a better way to do this, I will most likely change this in the future lol
    schedule.run_pending() 
    time.sleep(1) 