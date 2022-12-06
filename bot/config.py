import os


class Config:

    BOT_TOKEN = "5737688968:AAGq5Jk4CMp6tdFRH_aiOMIXz4mV7_A7__w"

    SESSION_NAME = ":memory:"

    API_ID = "17504802"

    API_HASH = "e9794fca6a58462b4d8fe2d988cffb2b"

    CLIENT_ID = "481149391142-8tf1dbsgmvola3voc7ellt1i5mnm8k4d.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    BOT_OWNER = "1311808931"

    AUTH_USERS_TEXT = "1311808931", ""

    AUTH_USERS = [BOT_OWNER, 1311808931] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
