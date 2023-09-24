class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 13305226 # integer value, dont use ""
    API_HASH = "8cde2475d6b0cb1162b89ebbac71a95d"
    TOKEN = "6592292827:AAHyz5q5MR9W_iRahcCjShG4UYRbCc-mRqw"    #is var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1258310642 # If you dont know, run the bot and do /id in your private chat with it, also an integer
   
    SUPPORT_CHAT = "wmteams" # Your own group for support, do not add the @
    START_IMG = "https://graph.org/file/c3d867beff6d043e74f1f.jpg"
    EVENT_LOGS = (-1001362823844)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://v:v@cluster0.zznxusa.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://yuxcwjtx:NufI2TI9hNdY2az8QWZdmZwHZCIHOjbo@peanut.db.elephantsql.com/yuxcwjtx"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "UX31XLHOBPL9KSGZ"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "OHBYT9I2Q0XH"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    CHATBOT_API="" # get it from @FallenChat_Bot using /token
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
