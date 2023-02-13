from flask import Flask, render_template
import datetime

app = Flask(__name__)

year = datetime.datetime.now().year

# main home page index
@app.route('/')
def index():
    year1 = year
    return render_template('index.html', year=year1)


# main page for test
@app.route('/test.html')
def test():
    return render_template('test.html')





if __name__ == "__main__":
    app.run(debug=True)