import vlc
import random
from typing import Optional


class Song:
    def __init__(self, name: str, composer: str, filepath: str, era: str, country: str, notes: Optional[str]):
        self.name = name
        self.composer = composer
        self.era = era
        self.country = country
        self.filepath = filepath
        self.notes = notes
        self.media = vlc.MediaPlayer(self.filepath)

    def play(self):
        self.media.play()

    def pause(self):
        self.media.pause()

    def stop(self):
        self.media.stop()

    def play_random(self):
        import time
        self.media.play()
        self.media.set_position(random.random())

    def __repr__(self):
        s = f"Name: {self.name}\nComposer: {self.composer}\nEra: {self.era}\nCountry: {self.country}"
        return f"{s}\nNotes: {self.notes}" if self.notes else s
