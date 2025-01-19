EMAIL = "glaciergoodness@gmail.com"
APP_PASSWORD = "nnci rqih vlio uneu"



import smtplib
from email.mime.text import MIMEText

html_body = """ 
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }
        .email-container {
            max-width: 600px;
            margin: 20px auto;
            background-color: #ffffff;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .header {
            background-color: #ff7f50;
            padding: 20px;
            text-align: center;
            color: #ffffff;
        }
        .header h1 {
            margin: 0;
            font-size: 28px;
        }
        .content {
            padding: 20px;
            text-align: center;
        }
        .content h2 {
            color: #ff7f50;
            margin-bottom: 10px;
        }
        .content p {
            font-size: 16px;
            color: #555555;
            margin-bottom: 20px;
        }
        .cta-button {
            display: inline-block;
            padding: 12px 20px;
            font-size: 16px;
            font-weight: bold;
            color: #ffffff;
            background-color: #ff7f50;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .cta-button:hover {
            background-color: #e06c40;
        }
        .footer {
            background-color: #eeeeee;
            padding: 10px;
            text-align: center;
            font-size: 14px;
            color: #777777;
        }
    </style>
</head>
<body>
    <div class="email-container">
        <div class="header">
            <h1>Ice Cream Heaven 🍦</h1>
        </div>
        <div class="content">
            <h2>Don't Forget Your Ice Cream!</h2>
            <p>Indulge in the creamiest, most delightful flavors, now available on our website. Treat yourself to the sweetness you deserve.</p>
            <a href="https://icecreamapp.onrender.com/" class="cta-button">Order Now</a>
        </div>
        <div class="footer">
            <p>© 2025 Ice Cream Heaven. All Rights Reserved.</p>
        </div>
    </div>
</body>
</html>
"""


msg = MIMEText(html_body,'html')

msg['from'] = EMAIL
msg['to'] = "jeebanjyotimallik01@gmail.com"
msg['subject'] = "We are here"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(EMAIL,APP_PASSWORD)
server.send_message(msg)
print('Mail sent..')
server.quit()
