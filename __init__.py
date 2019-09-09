# 初始化配置
import config as conf
import os
# bluetooth module
import blue
# Settings
isDebug = True

# Functions
def init_audio():
    conf.message('Initializing Audio Player.')
    import pyaudio as Player
    conf.audio_player = Player.PyAudio()

def init_audio_converter():
    conf.message('Initializing Audio Converter.')
    import ffmpeg,pydub
    conf.ffmpeg_engine = ffmpeg
    conf.pydub = pydub

def init_bluetooth():
    conf.message('Initializing Bluetooth Adapter.')
    import bluetooth
    conf.bluetooth_device = bluetooth
    # macOS TODO

def init_tmp_folder():
    conf.message('Initializing tmp folder.')
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
    # bluetooth module
    bluetooth_server = blue.ConnectionServer()
    # running threads
    bluetooth_server.start()
    
    