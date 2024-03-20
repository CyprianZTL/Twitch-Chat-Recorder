import irc.client
import sys

class TwitchChatClient(irc.client.SimpleIRCClient):
    def __init__(self, channel, target_user):
        super().__init__()
        self.channel = '#' + channel
        self.target_user = target_user.lower()  # Przechowuje nick użytkownika, którego wiadomości mają być wyświetlane

    def on_welcome(self, connection, event):
        connection.join(self.channel)

    def on_join(self, connection, event):
        print(f"Joined channel: {self.channel}")

    def on_pubmsg(self, connection, event):
        user = event.source.nick
        message = event.arguments[0]
        if user.lower() == self.target_user:  # Sprawdza, czy wiadomość pochodzi od docelowego użytkownika
            print(f"{user}: {message}")

def main():
    channel = 'Channel_Name'  # Nazwa kanału streamera
    nickname = 'Your_Nickname'  # Twój nick na Twitch
    token = 'Your_Twitch_authtoken'  # Twój token OAuth https://twitchtokengenerator.com/
    target_user = 'type_Target_Nick'  # Nick użytkownika, którego wiadomości chcesz przechwytywać

    client = TwitchChatClient(channel, target_user)
    try:
        client.connect('irc.chat.twitch.tv', 6667, nickname, password=f'oauth:{token}')
    except irc.client.ServerConnectionError:
        print("Could not connect to server.")
        sys.exit(1)

    client.start()

if __name__ == "__main__":
    main()
