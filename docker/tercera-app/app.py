from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabla = dynamodb.Table('tabla-CamiloAgudelo')

#Método para insertar elementos en una tabla de DynamoDB
@app.route('/insert', methods=['POST'])
def index():
  data = request.json
  item = {**data}

  tabla.put_item(Item=item)

  return 'Se guardó exitosamente!'

#Método para obtener un elemento de una tabla de DynamoDB por Id
@app.route('/get/<id>', methods=['GET'])
def get_item(id):
  try:
    response = tabla.get_item(Key={'id': id})

    if 'Item' in response:
      return jsonify(response['Item']), 200
    else:
      return jsonify({'Error': 'Item not found'}), 404
      
  except Exception as e:
    return jsonify({'Error': str(e)}),500

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
