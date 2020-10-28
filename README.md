# Attendance Form Auto-Submitter
 A python script to fill out and submit attendance form each day for distance learning and send a confirmation text.

## Motivation 
For distance learning we have to submit a Google Form for attendance everyday. While it's not difficult to do, it can be difficult to *remember* to do. This is a python script that automates the process and sends a text to confirm submission.

## Requirements
* [Python 3 or later](https://www.python.org/downloads/)
* [requests](https://pypi.org/project/requests/)
* [schedule](https://pypi.org/project/schedule/)
* [twilio](https://pypi.org/project/twilio/)

## Usage
1. Replace url on line 8 with the url of your Google Form
2. Replace the values to be submitted on lines 11-13 with your values, adding more variable if necessary.
3. Find the **entry id** for each value to be submitted and replace the entry ids on lines 16-21, adding more if needed.
    * Entry ids can be found by either right clicking on the question and selecting inspect element or by opening the Google Form in view-source by pushing `cmd+option+u` and scrolling to the bottom to find the ids
4. Create a [Twilio](https://www.twilio.com/) account to enable the text notifications.
    * Once your account is created, replace the account SID & auth token on line 27 with your own. Do the same for the phone numbers on lines 36 & 39.
5. If needed, change the time for the form to be submitted