### Remote Audio Player

Play Audio on your Linux devices using your phone.

**Requirements**

- Python Packages
  - pyaudio
  - pybluez
  - ffmpeg
- Linux Packages
  - libasoundr

**What you need to do**

- Download the [Release](https://github.com/Kingtous/RemoteAudioPlayer-Android/releases) App.
- Enter `bin` folder, run `build.sh` to compile sound adjustment binary executable file.
- Running `__init__.py` on your remote devices.
  - Linux Required
- Tip
You can also add .sevice in your systemd services of Linux. One of example is in the folder named "systemd-config".
### Q&A
- espeak doesn't work
  - maybe you are not using Jack(Like RaspberryPi). use `espeak "your sentences" --stdout | aplay` instead in `blue.py` and `tools.py`
