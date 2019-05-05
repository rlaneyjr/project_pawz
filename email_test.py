#!/usr/bin/env python

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *
import environ

env = environ.Env()
# reading .env file
env.read_env('.envs/.local/.django')

SENDGRID_API_KEY = env('SENDGRID_API_KEY', default=None)

sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
from_email = Email("test@example.com")
to_email = Email("rlaneyjr@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
