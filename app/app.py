from flask import Flask, render_template, request
from flask.helpers import url_for

from pytube import YouTube
import os

from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/')


def index():
    data = {
        'titulo':'Convertir MP3',
        'subtitulo':'Convertir Video De Youtube a Mp3'
    }
    return render_template('index.html', data=data)

@app.route('/converter', methods=['POST'])
def converter():
    
    if request.method == 'POST':
        url = request.form['url']

        try:
            """url = str(input("Ingrese URL del video: "))"""
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()

            out_file = video.download('/Users/michaelripoll/Downloads')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(yt.title + " Descarga exitosa.")

        except:
            print("Error al descargar.")
        return redirect(url_for('index'))

def pagina_no_encontrada(error):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)
