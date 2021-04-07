from flask import flash, Flask, render_template, redirect, request, url_for, jsonify
import ioc_fanger

app = Flask(__name__)
app.secret_key = 'abc'


@app.route("/")
def index():
    return render_template("index.html", version='3.2.2')


@app.route("/process", methods=['POST'])
def process_text():
    """Fang/defang indicators of compromise."""
    text = request.form['text']
    action = request.form['action']

    if not text:
        flash('Please enter some text.', 'error')
        return redirect(url_for('index'))
    else:
        if action == 'fang':
            processed_text = ioc_fanger.fang(text)
        else:
            processed_text = ioc_fanger.defang(text)
        return processed_text


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
