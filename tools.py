import config as conf
import os,time,wave
import __init__ as initializer

testAudio = 'ori.mp3'

def xxx2wav(path):
    if os.path.isfile(path) and conf.ffmpeg_engine != None and conf.pydub!=None:
        (basepath,filename,ext)=split_path(path)
        if ext == '.wav':
            return True
        try:
            sound = conf.pydub.AudioSegment.from_mp3(path)
            sound.export(path,format = 'wav')
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
            if conf.Stopped :
                # stop playing
                break
    except KeyboardInterrupt:
        pass
    finally:
        stream.close()
        conf.audio_player.terminate()
        initializer.init_audio()
        

def tts(text):
    os.system('espeak "'+text+'"')