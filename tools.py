import config as conf
import os,time,wave,sys
import __init__ as initializer

testAudio = 'ori.mp3'

def xxx2wav(path):
    if os.path.isfile(path) and conf.ffmpeg_engine != None and conf.pydub!=None:
        (basepath,filename,ext)=split_path(path)
        #if ext == '.wav':
        #    return True
        try:
            rename_path=basepath+'/'+filename+'.wav'
            os.system('/usr/bin/ffmpeg -y -i '+path+' -f wav '+rename_path)
            os.remove(path)
            os.rename(rename_path,path)
        except:
            # 可以试着播放
            return True
        return True
    else:
        print('Error Parsing',path)
        return False

def split_path(path):
    path,tfilename = os.path.split(path)
    filename,ext = os.path.splitext(tfilename)
    return (path,filename,ext)

def playAudio(path):
    conf.reset()
    if not xxx2wav(path):
        return
    wf = wave.open(path,'rb')
    stream = conf.audio_player.open(
        format = conf.audio_player.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )
    try:
        print('Start Playing.')
        conf.isPlaying = True
        data = wf.readframes(conf.chunk)
        while data != b'':
            stream.write(data)
            data = wf.readframes(conf.chunk)
            # User interrupted
            while conf.Interrupted :
                time.sleep(1)
            # stop playing
            if conf.Stopped :
                break
            if conf.VOL_UP:
                conf.increaseVolume()
            elif conf.VOL_DOWN:
                conf.decreaseVolume()
            
    except KeyboardInterrupt:
        pass
    finally:
        stream.close()
        conf.audio_player.terminate()
        initializer.init_audio()
        

def tts(text):
    os.system('espeak "'+text+'"')


