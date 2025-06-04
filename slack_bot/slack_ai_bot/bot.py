from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from datetime import date
import os
from dotenv import load_dotenv

load_dotenv()
app = App(token=os.getenv("SLACK_BOT_TOKEN"))


@app.event("app_mention")
def handle_mention(body, say):
    print("Got message:", body["event"]["text"])
    text = body["event"]["text"].lower()
    if "what is the date today" in text:
        say(f"Today is {date.today().strftime('%B %d, %Y')}")
    else:
        say("idk")


if __name__ == "__main__":
    handler = SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN"))
    handler.start()
