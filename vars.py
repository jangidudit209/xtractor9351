#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22946135"))
API_HASH = environ.get("API_HASH", "93e1b0c387cabe34a3ccfa1724ae8527")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "1368753935"))
CREDIT = "𝗔𝗗𝗜𝗧𝗬𝗔⚡"
AUTH_USER = os.environ.get('AUTH_USERS', '7062964338,6305120550').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
