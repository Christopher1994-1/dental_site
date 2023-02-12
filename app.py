from flask import Flask, render_template

app = Flask(__name__)



# main home page index
@app.route('/')
def index():
    return render_template('index.html')


# main page for test
@app.route('/test.html')
def test():
    return render_template('test.html')





if __name__ == "__main__":
    app.run(debug=True)