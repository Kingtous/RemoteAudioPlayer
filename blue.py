import bluetooth
import threading
import config as conf
import os,tools,json
uuid = "fa288726-b927-4c4e-bf4b-f616f386332d"

def startBT():
    while True:
        try:
            tried = False
            isJson = False
            server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            server_sock.bind(("", bluetooth.PORT_ANY))
            server_sock.listen(1)
            port = server_sock.getsockname()[1]
            bluetooth.advertise_service(server_sock,"Audio Player",service_id=uuid)
            conf.message('Waiting for connection')
            # TODO 加段音频，等待连接
            # os.system('espeak "wating for connection."')
            client_sock,client_info = server_sock.accept()
            # TODO 加段音频，连接成功
            # os.system('espeak "connection success."')
            data = None
            tmp_file_path = conf.tmp_path+'/'+'tmp.mp3'
            if not conf.isPlaying:
                file_holder = open(tmp_file_path,'wb+')
            while True:
                data = client_sock.recv(1024)
                if len(data) == 0:
                    break
                # 尝试转json，看看是不是指令
                if not tried:
                    try:
                        act = json.loads(bytes.decode(data,encoding='utf-8'))
                        if act.get('act',False):
                            action_str = act.get('act','None')
                            if action_str == 'play':
                                tools.tts('music playing')
                                conf.Interrupted = False
                            elif action_str == 'pause':
                                tools.tts('music paused')
                                conf.Interrupted = True
                            elif action_str == 'stop':
                                tools.tts('music stopped')
                                conf.Stopped = True
                            break
                    except UnicodeDecodeError:
                        pass
                    except AttributeError:
                        pass
                    finally:
                        tried = True
                # 写入临时文件
                if not conf.Stopped and conf.isPlaying:
                    import time
                    conf.Stopped = True
                    time.sleep(0.2)
                if file_holder.closed:
                    file_holder = open(tmp_file_path,'wb+')
                file_holder.write(data)
            if not file_holder.closed:
                file_holder.close()
        except KeyboardInterrupt:
            break
        except IOError:
            file_holder.close()
            if not isJson:
                player = AudioPlayer(tmp_file_path)
                player.start()
        finally:
            client_sock.close()
            server_sock.close()


class AudioPlayer(threading.Thread):
    def __init__(self,path):
        super().__init__()
        self.path = path

    def run(self):
        tools.playAudio(self.path)

class ConnectionServer(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        import __init__ as initializer
        initializer.init()
        startBT()

if __name__ == "__main__":
    import __init__ as initializer
    initializer.init()
    startBT()
