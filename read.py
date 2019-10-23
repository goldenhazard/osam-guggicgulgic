import sys
import serial
import serial.tools.list_ports
import time
import requests
import audioop
from pydub import AudioSegment

def get_text():
    audio_q = b''
    buff_size = 2048

    ports = list(serial.tools.list_ports.comports())
    print(ports);

    for p in ports:
        print(p);
        if 'ttyACM1' in p[1]: 
            com_port = p[0]
            break;
        else: com_port = ''
    try:
        port = serial.Serial(com_port,230400,timeout=None)
    except:
        print("Connection Error: Can't find Arduino serial port")
        sys.exit()
    millis = int(round(time.time() * 1000))
    while(int(round(time.time()*1000))-millis<=5000):
        rec_bytes = port.read(buff_size)
        audio_q+=rec_bytes

    audio_q=audioop.mul(audio_q,1,3)

    sound = AudioSegment(
        data=audio_q,
        sample_width=1,
        frame_rate=20000,
        channels=1
    )
    sound.export("audio.mp3",format="mp3")
    files = open('audio.mp3', 'rb')

    upload = {'file':files}
    res = requests.post('http://kclee.run-us-west1.goorm.io/upload', files = upload)
    print(res.text)
    return res.text

