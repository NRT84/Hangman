from pynput import keyboard


class Events:

    def __init__(self, configuration):
        self.config = configuration
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.start_listener()

    def start_listener(self):
        self.listener.start()

    def stop_listener(self):
        self.listener.stop()

    def on_press(self, key):
        if key == keyboard.Key.f1:
            print("\n{}\nEnter your guess: ".format(self.config.question))
