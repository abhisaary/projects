from flask import Flask
from flask import request
import json

app = Flask(__name__)

# Accepts json data with two ints x,y -- returns sum in json format
@app.route("/test", methods=['POST'])
def jsonPOST():
	content = request.get_json()
	sum_ = content['x'] + content['y']
	ret = json.dumps({'sum': sum_})
	return ret

if __name__ == "__main__":
	app.run()