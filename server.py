from flask import Flask, request, jsonify, make_response
from flask_cors import CORS 
import json
from CNN.prediction import predict
from NLP.chat import get_response

app = Flask(__name__)
CORS(app)

images = [
  { 'name': 'some img', 'url': 'www.google.com' }
]

ret_obj = [
  { 'reverse': 'qwoioiad.eqowp' }
]


@app.route('/')
def home():
  return "<h1>Welcome to Flask Server!<h1>"

@app.route('/api/images')
def get_images():
  return jsonify(images)


@app.route('/api/images', methods=['POST'])
def add_image():
  data_str = request.get_data(parse_form_data=True).decode('ascii')
  data = json.loads(data_str)
  print(data['url'])
  #data = request.get_json()
  #print(data)
  img_url = data['url']
  result = predict(img_url)
  result = result.tolist()
  #prob = {'neg': result[0], 'pos': result[1]}
  neg = json.dumps(result[0][0])
  pos = json.dumps(result[0][1])
  response = make_response(
                jsonify({ 'neg': neg, 'pos': pos }),
                200,
            )
  response.headers["Content-Type"] = "application/json"
  return response

@app.route('/api/chat', methods=['POST'])
def bot_response():
  data_str = request.get_data().decode('ascii')
  data = json.loads(data_str)
  user_input = data['msg']
  pos = float(data['pos'])
  neg = float(data['neg'])
  reply = get_response(user_input, pos, neg)
  response = make_response(jsonify({'reply': reply}),200)
  response.headers['Content-Type'] = 'application/json'
  return response


if __name__ == '__main__':
    app.run(debug=True)