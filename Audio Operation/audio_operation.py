import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3
from pydub import AudioSegment
import pygame
import matplotlib.pyplot as plt
import numpy as np

# Helper function to check if file exists
def file_exists(file_name):
    if not os.path.exists(file_name):
        print(f"Error: {file_name} does not exist.")
        return False
    return True

def get_mp3_metadata(file_name):
    if not file_exists(file_name):
        return
    audio = MP3(file_name, ID3=ID3)
    duration = audio.info.length
    bitrate = audio.info.bitrate
    artist = audio.tags.get("TPE1", ["Not available"])[0]
    print(f"Duration: {duration:.2f} sec")
    print(f"Bitrate: {bitrate} bps")
    print(f"Artist: {artist}")

def convert_mp3_to_wav(file_name, output_name):
    if not file_exists(file_name):
        return
    try:
        audio = AudioSegment.from_mp3(file_name)
        audio.export(output_name, format="wav")
        print("MP3 file converted to WAV successfully!")
    except Exception as e:
        print(f"Error: {e}")

def play_two_mp3s(file1, file2):
    if not file_exists(file1) or not file_exists(file2):
        return
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file1)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.load(file2)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    print("Both MP3 files played in sequence")

def edit_mp3_metadata_and_plot(file_name):
    if not file_exists(file_name):
        return
    audio = EasyID3(file_name)
    audio["title"] = "Modified Song"
    audio["artist"] = "New Artist"
    audio["album"] = "Modified Album"
    audio.save()
    print("Metadata updated successfully!")

    sound = AudioSegment.from_mp3(file_name)
    samples = np.array(sound.get_array_of_samples()[::100])  # Reduce sample size
    duration = len(samples) / sound.frame_rate
    time_axis = np.linspace(0, duration, num=len(samples))

    plt.figure(figsize=(12, 4))
    plt.plot(time_axis[:5000], samples[:5000], label="Audio Waveform", color="blue")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("Modified MP3 Waveform")
    plt.legend()
    plt.show()

# Main switch-case structure
def main():
    print("Choose an option:")
    print("1. Get MP3 Metadata")
    print("2. Convert MP3 to WAV")
    print("3. Play Two MP3 Files in Sequence")
    print("4. Edit MP3 Metadata and Plot Waveform")
    
    choice = int(input("Enter choice (1-4): "))
    
    match choice:
        case 1:
            get_mp3_metadata("audio.mp3")
        case 2:
            convert_mp3_to_wav("audio.mp3", "converted_audio.wav")
        case 3:
            play_two_mp3s("audio.mp3", "another_audio.mp3")
        case 4:
            edit_mp3_metadata_and_plot("audio.mp3")
        case _:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
