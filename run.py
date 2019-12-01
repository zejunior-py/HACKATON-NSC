# import speech_recognition as sr
# import soundfile as sf
#
# file_audio_ogg = 'database/audio_brenda.ogg'
# file_audio_wav = 'database/out.wav'
# r = sr.Recognizer()
# with sr.AudioFile(file_audio_wav) as source:
#     audio = r.listen(source)
#
# print(r.recognize_google(audio, language='pt-BR'))
from datetime import date

LOCAL = 'database/tot.txt'
A = 1574879999
B = 1575249999

timestamp = date.fromtimestamp(A)
timestamp2 = date.fromtimestamp(B)

with open(LOCAL, 'w') as r:
    for i in range(A, B, 50):
        r.writelines(str(i)+'\n')
r.close()
print("Date =", timestamp, B - A)
