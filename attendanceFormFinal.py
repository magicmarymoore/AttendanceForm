import requests #to submit the form
import schedule #to have it submit the form on the correct days
import time #to have a little break
from twilio.rest import Client

url = 'https://docs.google.com/forms/d/e/1FAIpQLSfMTRk4rwE41-tmaDv-QxUJvHrvNDfQeCqXHRlVbA29gJ-fcg/viewform' #url of google form to be filled out
finalData = [] #list that will eventually hold all data to be submitted
#values ot be submitted (don't have to be variables tho...)
lastname = 'Moore'
firstname = 'Mary'
inschool = 'Yes'

values = { #"entry.number": value --> each question on the form has it's own unique id
            # last name
            "entry.2111526481": lastname,
            # first name
            "entry.1919488153": firstname,
            # attending classes??
            "entry.1847612170": inschool,
        }
finalData.append(values) #add the data to the list

client = Client("AC50d889a7d2c262e728951e29cda0bdb7", "30bbb5bc5d7e117ef93a9ee87e286bb1")
def sendAttendance(url, data):
    for d in data:
        try:
            requests.post(url, data=d) #subit the form
            print("form submitted")
            client.messages.create(to="+12186562444", from_="+12053017261", body="form submitted")
        except:
            print("error!")
            client.messages.create(to="+12186562444", from_="+12053017261", body="error!")

#sendAttendance(url, finalData)

def workpls(): #b/c the schedule thing was weird and couldn't run a function w/params or smth...
    sendAttendance(url, finalData)

#only need to fill out the form on mon-wed
schedule.every().monday.at("08:00").do(workpls)
schedule.every().tuesday.at("08:00").do(workpls)
schedule.every().wednesday.at("08:00").do(workpls)

while True: #do the things, all the time --> this is probably overkill, there is most definately a better way to do this, I will most likely change this in the future lol
    schedule.run_pending() 
    time.sleep(1) 