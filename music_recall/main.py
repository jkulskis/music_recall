import glob
import os
import sys
import random
from recall import Song
from typing import List


def play_songs(
    songs: List[Song], play_random_timestamp: bool = True, enter_info: bool = False
):
    while 1:
        song = random.choice(songs)
        if play_random_timestamp:
            song.play_random()
        else:
            song.play()
        if input("Press Enter to Stop Playing, q to quit: ").lower() == "q":
            print("Thanks for listening!")
            return
        song.stop()
        if enter_info:
            input("Composer: ")
            input("Name: ")
            input("Era: ")
            input("Country: ")
        print(f"\n{song}\n")
        input("Press Enter for the next song")


if __name__ == "__main__":
    song_dir = ""
    if len(sys.argv) > 2:
        raise ValueError("Too many CLI args")
    elif len(sys.argv) == 2:
        song_dir = sys.argv[1]
    else:
        song_dir = input("Song dir: ")
    songs = []
    for song_filepath in [os.path.abspath(x) for x in glob.glob(f"{song_dir}/*.mp3")]:
        filename_split = os.path.basename(song_filepath).split("_")
        filename_split[-1] = filename_split[-1][:-4]  # get rid of .mp3
        if len(filename_split) == 4:
            filename_split.append("")
        composer, name, era, country, notes = filename_split
        songs.append(
            Song(
                name=name,
                composer=composer,
                filepath=song_filepath,
                era=era,
                country=country,
                notes=notes,
            )
        )
    play_songs(
        songs=songs,
        play_random_timestamp=False
        if input(
            "Enter 0 to play from the beginning, otherwise random timestamp will be chosen: "
        )
        == "0"
        else True,
        enter_info=input("Enter 0 to prompt for info after listening: "),
    )
