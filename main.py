
from pytube import YouTube
import os

try:
    url = str(input("Ingrese URL del video: "))
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download('/Users/michaelripoll/Downloads')
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(yt.title + " Descarga exitosa.")

except:
    print("Error al descargar.")