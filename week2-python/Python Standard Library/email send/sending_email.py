from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template

template = Template(Path("template.html").read_text())
# template.substitute()

message = MIMEMultipart()
message["from"] = "Test user"
message["to"] = "test@gmail.com"
message["subject"] = "Test message"
body = template.substitute({"name": "John"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("images.jpg").read_bytes()))
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("test@gmail.com", "asfaw212Q!")
    smtp.send_message(message)
    print("Sent...")
