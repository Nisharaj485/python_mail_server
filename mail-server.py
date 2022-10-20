import smtplib
sender_email = input("enter your sender email  :")
sender_password = input("enter your password  :")
message = input("enter your message  :")
receiver_email = input("enter sender email  :")

# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication

s.login(sender_email, sender_password) # enter your generated gmail app password not your gamil password

# message to be sent


# sending the mail

s.sendmail(sender_email, receiver_email, message )

# terminating the session
s.quit()
print("mail sent successfully")
