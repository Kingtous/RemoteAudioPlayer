import config as conf
import os
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
    else:
        print('Error Parsing',path)
        return False

def split_path(path):
    path,tfilename = os.path.split(path)
    filename,ext = os.path.splitext(tfilename)
    return (path,filename,ext)
