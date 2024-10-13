from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    global name
    name = request.form['name']
    email = request.form['email']
    feedback = request.form['feedback']
    rating = request.form['rating']

    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
