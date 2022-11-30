import os



class Config(object):
      BOT_TOKEN = "5762860961:AAHmkOuM23UibNupEbSnig9CjObJtYDIdJg"
      API_ID = 5080899
      API_HASH = "6fc7f813cf96e6692990b752b43fd9c7"
      CAPTION_POSITION = "bottom"
      ADMIN_USERNAME = hellohoney
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 123476535 )) 
      DB_URL = os.environ.get("DATABASE_URL", "")
