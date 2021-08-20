from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/google-charts/bar-chart')
def google_bar_chart():
    data = {'Currency' : 'USD', 'exchange_timezone' : 'America/New_York', 'type' :'Common Stock'}
    return render_template('bar-chart.html', data=data)



if __name__ == "__main__":
    app.run()