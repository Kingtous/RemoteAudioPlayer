# portaudio
echo -e 'checking portaudio...\n'
sudo pacman -S portaudio.dev espeak
# pip3
echo -e 'resolving python dependencies...\n'
sudo pip3 install pyaudio ffmpeg pybluez
# /var/lib/systemd/system/bluetoothd -E -C
