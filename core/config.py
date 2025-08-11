import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

DB_CONFIG = {
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "port": os.getenv("DB_PORT"),
    "host": os.getenv("DB_HOST"),
    "password": os.getenv("DB_PASS")
}
