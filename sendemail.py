def send_email():
   import smtplib
   from smtplib import SMTPException

   import csv
   #condition to check and send email if value remains true
   value = 1
   # put the files contents in a list
   content = []
   with open('update.csv','r') as t1:
      # check if the file is empty or not
      t1.seek(0)
      first_char = t1.read(1)
      if not first_char:
         print('File is empty')
         value = 0
      #if the file contains someting send email
      data = csv.reader(t1)
      for row in data:
         print(row)
         content.append(row)
      t1.close()
   # send the email
   print(value)
   if value != 0:
      sender = 'spa.emarketing@gmail.com'
      receivers = ['lightstona@gmail.com','info@liquorworld.com.np','smritispa001@gmail.com','kailash.sherpagroup@gmail.com']
      message = str(content).encode()

      try:
         smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
         print('connecting')
         smtpObj.login("spa.emarketing@gmail.com", "sherpa1976")
         print('connected..')
         smtpObj.sendmail(sender, receivers, message)
         print ("Successfully sent email")
         smtpObj.quit()
      except smtplib.SMTPException as e:
         print ("Error: unable to send email",e)

