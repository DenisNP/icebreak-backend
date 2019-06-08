import sys
from flask import Flask, request
from flask_cors import CORS, cross_origin
from gamestate import GameState

# init
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# sessions
sessions = {}

# return game state
@app.route('/gamestate', methods=['POST'])
@cross_origin()
def gamestate_json():
    #req_data = request.get_json()
    #user_action = req_data['user_action']['param1']
    #last_process_timestamp = req_data['last_process_timestamp']
    id = str(request.args.get('id'))

    if id and (id in sessions):
        session = sessions[id]
        return session.to_json()
    else:
        session = GameState()
        sessions[session.id] = session
        return session.to_json()

if __name__ == '__main__':
    app.run(debug=True, port=5000)  #run app in debug mode on port 5000
    
    