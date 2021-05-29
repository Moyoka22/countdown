import threading

from readchar import readchar

from .Countdown import Countdown


class Listener(threading.Thread):
    def __init__(self, countdown: Countdown):
        super().__init__(target=self.listen, daemon=True, name='listener')
        self._countdown = countdown

    def listen(self):
        while 1:
            try:
                user_input = readchar()
                if user_input == 'p':
                    if self._countdown.is_paused():
                        self._countdown.unpause()
                    else:
                        self._countdown.pause()
                if user_input == 'c':
                    self._countdown.end()
            except KeyboardInterrupt:
                self._countdown.end()
