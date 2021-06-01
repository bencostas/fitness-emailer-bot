import gspread

from datetime import date

import smtplib, ssl

#Server = 'localhost'

gc = gspread.service_account(filename='xxx.json') #json file containing the google cloud service credentials

worksheet = gc.open_by_key('xxx').sheet1 # sheet ID

# Get data from spreadsheet
def getDF(col: int) -> str:
    message = "- 12PM -\n"
    message = message + worksheet.cell(3, col).value
    message = message +"\n\n- 3PM -\n"
    message = message + worksheet.cell(4, col).value
    message = message +"\n\n- 6PM -\n"
    message = message + worksheet.cell(5, col).value
    message = message +"\n\n- 9PM -\n"
    message = message + worksheet.cell(6, col).value
    message = message +"\n\n- Workout -\n"
    message = message + worksheet.cell(7, col).value
    return message

# Check today's date
today = date.today().weekday()

# If ... date:
message = ''
# Sunday
if (today == 6):
    message = getDF(2)
# Monday
elif (today == 0):
    message = getDF(3)
# Tuesday
elif (today == 1):
    message = getDF(4)
# Wednesday
elif (today == 2):
    message = getDF(5)
# Thursday
elif (today == 3):
    message = getDF(6)
# Friday
elif (today == 4):
    message = getDF(7)
# Saturday
elif (today == 5): 
    message = getDF(8)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sender@gmail.com"  # Enter the sender's email address
receiver_email = "recipients@gmail.com"  # Enter receiver's email address
# enter the password for the sender_email
password = 'password'
message = "Subject: Today\'s Workout:\n" + message
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
