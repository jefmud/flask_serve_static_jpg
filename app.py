from flask import Flask, send_file
import io
import os

FILE_PATH = '/Users/bio/Desktop/LONG_TERM_PLOT_PHOTOS/'
app = Flask(__name__, static_url_path=FILE_PATH)

@app.route('/')
def index():
    return "here"

@app.route('/media/<path:path>')
def serve_media(path):
    pathname = os.path.join(FILE_PATH, path)
    if os.path.isdir(pathname):
        buf = os.listdir(pathname)
        return str(buf)
    elif os.path.isfile(pathname):
        with open(pathname, 'rb') as fp:
            if '.jpg' in pathname.lower():
                return send_file(
                    io.BytesIO(fp.read()),
                    attachment_filename='image.jpg',
                    mimetype='image/jpg'
                )
            else:
                "only allowed to serve jpg files"
    else:
        return "nothing to see here"

if __name__ == '__main__':
    app.run(debug=True)