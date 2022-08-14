from InternetSpeed import InternetSpeedTwitterBot
PROMISED_DOWN = 200
PROMISED_UP = 10
EMAIL = "REDACTED"
PASSWORD = "REDACTED"

bot = InternetSpeedTwitterBot()

list = bot.get_intern_speed()
actual_down = list[0]
actual_up = list[1]

if actual_down < PROMISED_DOWN or actual_up < PROMISED_UP:
    bot.tweet_at_provider(actual_down=actual_down, actual_up=actual_up, email=EMAIL, password=PASSWORD)
else:
    print("all good")
bot.close()
