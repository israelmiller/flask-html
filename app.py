from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default_home():
    return render_template('home_page.html')

@app.route('/patients')
def patients():
    return render_template('patient_page.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
