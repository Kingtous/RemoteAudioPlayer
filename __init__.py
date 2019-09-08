# 初始化配置
import config as conf
import os
# Settings
isDebug = True

# Functions
def message(text):
    if isDebug:
        print(text)

def init_audio():
    message('Initializing Audio Player.')
    import pyaudio as Player
    conf.audio_player = Player.PyAudio()

def init_audio_converter():
    message('Initializing Audio Converter.')
    import ffmpeg,pydub
    conf.ffmpeg_engine = ffmpeg
    conf.pydub = pydub

def init_bluetooth():
    message('Initializing Bluetooth Adapter.')
    # macOS TODO

def init_tmp_folder():
    message('Initializing tmp folder.')
    if not os.path.exists(conf.tmp_path):
        os.mkdir(conf.tmp_path)

def init():
    init_audio()
    init_audio_converter()
    init_bluetooth()
    init_tmp_folder()
    # TODO Threading


if __name__ == '__main__':
    init()