import os
from flask import Flask, jsonify
# instantiate the app
app = Flask(__name__)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object('project.config.DevelopmentConfig')

#print(app.config)
@app.route('/users/ping', methods=['GET'])
def ping_pong():
 return jsonify({
  'status': 'success',
  'message': 'pong!'
 })
