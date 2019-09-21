# Variable
audio_player = None
bluetooth_device = None
ffmpeg_engine = None
pydub = None

# 临时Path
tmp_path = '/tmp/remoteAudio'

# configuration
chunk = 4096
Interrupted = False
Stopped = False
isVerbose = True

# arg
import os,sys
vctool = os.path.split(sys.argv[0])[0]+'/bin/vc '


def increaseVolume():
    os.system(vctool+' -i')

def decreaseVolume():
    os.system(vctool+' -d')



# status
isPlaying = False

# temper option
VOL_UP = False
VOL_DOWN = False


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
