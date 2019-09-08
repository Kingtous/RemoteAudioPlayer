# Variable
audio_player = None
bluetooth_device = None
ffmpeg_engine = None
pydub = None

# 临时Path
tmp_path = '/tmp/remoteAudio'

# configuration
chunk = 1024
Interrupted = False
Stopped = False
isVerbose = True

# status
isPlaying = False


def message(text):
    if isVerbose:
        print(text)

def reset():
    global Interrupted,Stopped,isPlaying
    Interrupted = False
    Stopped = False
    isPlaying = False

"""
命令：
{action:'xxx',value:0}

pause:暂停
play:播放

"""