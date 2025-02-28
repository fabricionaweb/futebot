import os

BOT_ENV = os.getenv("BOT_ENV")
BOT_ENV_DEV = "dev"
BOT_ENV_PROD = "prod"
BOT_PROD_PREFIX = "."
BOT_DEV_PREFIX = ","

AVAILABLE_SPOILER_ACTIONS = ["--spoiler", "--nsfw"]

CHARADA_ENDPOINT = "https://us-central1-kivson.cloudfunctions.net/charada-aleatoria"
COACH_ENDPOINT = (
    "http://api.forismatic.com/api/1.0/?method=getQuote&key=457653&format=json&lang=en"
)
YT_RESULTS_ENDPOINT = "http://www.youtube.com/results?"
YT_WATCH_ENDPOINT = "http://www.youtube.com/watch?v="
HOROSCOPO_ENDPOINT = "http://babi.hefesto.io/signo/{}/dia"
DICTIONARY_PTBR_ENDPOINT = "http://dicionario-aberto.net/search-json/{}"
WEATHER_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={}&appid={}"
LMGTFY_ENDPOINT = "http://tinyurl.com/api-create.php?url=http://letmegooglethatforyou.com/?q={}"

IMGUR_CLIENT_ID = os.getenv("IMGUR_CLIENT_ID")
IMGUR_CLIENT_SECRET = os.getenv("IMGUR_CLIENT_SECRET")

DISCORD_EMBED_LIMIT = 25
