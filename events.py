from pynput import keyboard


class Events:

    def __init__(self, configuration):
        self.config = configuration
    #     self.init_listener()
    #
    # def init_listener(self):
    #     listener = keyboard.Listener(on_press=self.on_press)
    #     listener.start()
    #
    # def on_press(self, key):
    #     if key == keyboard.Key.f1:
    #         print("\n{}\nEnter your guess: ".format(self.config.question))
