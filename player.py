import pyaudio as aplayer
import wave
import config as conf
import tools
import os

testAudio = '/Users/kingtous/PycharmProjects/remote_audio_play/ori.mp3'

def playAudio(path):
    if not tools.xxx2wav(path):
        return
    wf = wave.open(path,'rb')
    stream = conf.audio_player.open(
        format = conf.audio_player.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True
    )
    try:
        data = wf.readframes(conf.chunk)
        while data != '':
            stream.write(data)
            data = wf.readframes(conf.chunk)
            # User interrupted
            if conf.Interrupted :
                break
    except KeyboardInterrupt:
        pass
    finally:
        stream.close()
        conf.audio_player.terminate()

    
if __name__ == '__main__':
    import __init__ as initializer
    initializer.init()
    playAudio(testAudio)
    pass