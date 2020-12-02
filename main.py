import pickle
from flask import Flask, request, jsonify, Response
from model_files.ml_model import predict_hardhat
import requests
import json
import sys

token = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjkyMDk4ODk4LCJ1aWQiOjE3MTA5NTE3LCJpYWQiOiIyMDIwLTExLTI3VDE1OjU2OjM3LjAwMFoiLCJwZXIiOiJtZTp3cml0ZSJ9.zL37upgnVE-E4Ps0L3boEto9x_h-2nMopy8Gf7i-eag'
myurl = 'https://david-klett-team.monday.com/v2/'
header = {
"Accept": "*/*",
"Content-Type": "application/json",
"Authorization": "{}".format(token),
} 

##creating a flask app and naming it "app"
app = Flask('app')

@app.route('/test', methods=['GET'])
def test():
    return 'Pinging Model Application!!'

@app.route('/webhook', methods=['POST'])
def predict():
    payload = request.get_json()
    print(payload)
    sys.stdout.flush()
    assetid = payload["event"]["value"]["files"][0]["assetId"]
    #boardid = payload.event.boardId
    itemid = payload["event"]["pulseId"]
    print("asset id:",assetid)
    sys.stdout.flush()
    # graphql api
    query = """query {
        assets(ids:%d){
            id
            public_url
        }
    }""" % (assetid)
    r = requests.post(myurl,headers=header,json={'query': query}).text
    myobject = json.loads(r)
    # get the public url of the image asset
    image_url = myobject["data"]["assets"][0]["public_url"]
    print(image_url)
    sys.stdout.flush()
    
    image_data = requests.get(image_url).content
    # with open('./model_files/image_name.jpg', 'wb') as handler:
    #     handler.write(image_data)
    # predictions = predict_hardhat('image_name.jpg')
    # #predictions = picture
    # result = {
    #     'hard hat predictions': (predictions)
    # }
    # if predictions == hardhat then call graphql
    query2 = """mutation {
        change_simple_column_value (board_id: 870269962, item_id: %d, column_id: "status", value: "1") {
            id
        }
    }""" % (itemid)
    # post to graphql api
    r = requests.post(myurl,headers=header,json={'query': query2})
    return request.json

# @app.route('/webhook', methods=['POST'])
# def respond():
#     print(request.json)
#     return request.json

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=9696)

