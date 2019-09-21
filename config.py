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

# status
isPlaying = False

# temper option
VOL_UP = False
VOL_DOWN = False

# arg
import os,sys
vctool = os.getcwd()+'/bin/vc '


def increaseVolume():
    global VOL_UP
    os.system(vctool+' -i')
    VOL_UP = False

def decreaseVolume():
    global VOL_DOWN
    os.system(vctool+' -d')
    VOL_DOWN = False


def message(text):
    if isVerbose:
        print(text)

def reset():
    global Interrupted,Stopped,isPlaying,VOL_DOWN,VOL_UP
    Interrupted = False
    Stopped = False
    isPlaying = False
    VOL_UP = False
    VOL_DOWN = False

"""
命令：
{action:'xxx',value:0}

pause:暂停
play:播放

"""
