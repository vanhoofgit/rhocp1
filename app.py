from flask import Flask
from flask.templating import render_template
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')

def main():
    app.run()


if __name__ == '__main__':
    main()
