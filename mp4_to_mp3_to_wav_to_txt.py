from pydub import AudioSegment
import speech_recognition as sr
from moviepy.editor import *
import math

# mp4 to mp3
video = VideoFileClip("video.mp4")
video.audio.write_audiofile("example.mp3")

# convert mp3 file to wav
src=("example.mp3")
sound = AudioSegment.from_mp3(src)
sound.export("example.wav", format="wav")
file_audio = sr.AudioFile(r"example.wav")

# use the audio file as the audio source
r = sr.Recognizer()

# B: from wac
with file_audio as source:
   audio = r.record(source)
result = r.recognize_google(audio, language='yue')

try:
    print("Transcription: " + result)   # recognize speech using Google Speech Recognition
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")

# because the r.recognize_google only can recognize 5 - 15 seconds, you need to split the wac first

class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '/' + filename

        self.audio = AudioSegment.from_wav(self.filepath)

    def get_duration(self):
        return self.audio.duration_seconds

    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '/' + split_filename, format="wav")

    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename
            self.single_split(i, i + min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')

folder = "/Users/chutszkan/Documents/Code/Git/autosub_try"
file = "example.wav"
split_wav = SplitWavAudioMubin(folder, file)
split_wav.multiple_split(min_per_split=1)

for i in range(0, 3):
    print(i)
    try:
        file_audio = sr.AudioFile(f"{i}_example.wav")
        with file_audio as source:
            audio = r.record(source)
        result = r.recognize_google(audio, language='yue')
        print("Transcription: " + result)
    except:
        print('not recognize')
        pass
    
# success but need to split the video when people speak
