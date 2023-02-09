import os
from flask import Flask, redirect, render_template, request, url_for
import PIL
import pilgram

app = Flask(__name__)

UPLOAD_FOLDER = '/workspaces/54048627/final-project/static/flask_image/raw'

FILTERS = ["Aden", "Brannan", "Brooklyn", "Clarendon", "Earlybird", "Gingham", "Hudson", "Inkwell", "Kelvin"]

filter_methods = {
    FILTERS[0]: pilgram.aden,
    FILTERS[1]: pilgram.brannan,
    FILTERS[2]: pilgram.brooklyn,
    FILTERS[3]: pilgram.clarendon,
    FILTERS[4]: pilgram.earlybird,
    FILTERS[5]: pilgram.gingham,
    FILTERS[6]: pilgram.hudson,
    FILTERS[7]: pilgram.inkwell,
    FILTERS[8]: pilgram.kelvin
}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'jpg', 'png'}

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        if 'picture' not in request.files:
            return redirect("/")

        file = request.files['picture']

        if file.filename == '':
            return redirect("/")

        if request.form.get("filters") not in FILTERS:
            return redirect("/")

        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "raw.jpg"))

            img = PIL.Image.open("/workspaces/54048627/final-project/static/flask_image/raw/raw.jpg")

            func = filter_methods.get(request.form.get("filters"))

            if func is not None:
                func(img).save("/workspaces/54048627/final-project/static/flask_image/filtered/filtered.jpg")

            return render_template("filtered.html")

        return redirect("/")

    else:
        return render_template("index.html", filters=FILTERS)