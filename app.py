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
    id = ''
    try:
        req_data = request.get_json()
        id = req_data['id']
    except:
        id = ''

    if id and not (id in sessions):
        return '{"error": "No session found"}'

    if id and (id in sessions):
        session = sessions[id]
        session.update_all()
        return session.to_json()
    else:
        session = GameState()
        sessions[session.id] = session
        session.update_all()
        return session.to_json()

if __name__ == '__main__':
    app.run(debug=True, port=5000)  #run app in debug mode on port 5000
    
    