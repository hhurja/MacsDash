from flask import Flask, request

app = Flask(__name__)

@app.route('/api')
def api_root():
	return 'hello and welcome to the MacsDash API'

if __name__ == '__main__':
	app.run()

