from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    with open('static/bio.txt', 'r') as bio_file:
        bio_content = bio_file.read()
    return render_template('index.html', bio_content=bio_content)


if __name__ == '__main__':
    app.run(debug=True)
