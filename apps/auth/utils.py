import psycopg2
import random
from datetime import datetime
from core.database import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_random_code(email: str):
    try:
        conn = get_db_conn()
        cursor = conn.cursor()

        while True:
            random_code = str(random.randint(1000, 9999))


            cursor.execute("SELECT 1 FROM codes WHERE code = %s;", (random_code,))
            exists = cursor.fetchone()

            if not exists:
                break


        cursor.execute(
            "INSERT INTO codes (code, email) VALUES (%s, %s);",
            (random_code, email)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return random_code

    except psycopg2.Error as e:
        print("Database error:", e)
        return None

def send_mail(receiver_email, body):
    sender_email = "sanjarbeksocial@gmail.com"
    password = "ajvd xsnx jowk hujh"

    subject = "Confirmation code"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Code sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

