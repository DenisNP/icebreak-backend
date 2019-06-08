from flask import Flask, request  #import main Flask class and request object
import sys
from gamestate import GameState

app = Flask(__name__) #create the Flask app
temp_state = GameState()

@app.route('/gamestate', methods=['POST']) #GET requests will be blocked
def gamestate_json():

    req_data = request.get_json()

    id = request.args.get('id')
    #user_action = req_data['user_action']['param1']
    #last_process_timestamp = req_data['last_process_timestamp']

    return temp_state.to_json()

if __name__ == '__main__':
    app.run(debug=True, port=5000)  #run app in debug mode on port 5000
    
    