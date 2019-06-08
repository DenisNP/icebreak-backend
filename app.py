from flask import Flask, request  #import main Flask class and request object
import sys
app = Flask(__name__) #create the Flask app

@app.route('/gamestate', methods=['POST']) #GET requests will be blocked
def gamestate_json():

    req_data = request.get_json()

    #print(request.args, file=sys.stderr)

    user_id = request.args.get('user_id')
    user_action = req_data['user_action']['param1']
    last_process_timestamp = req_data['last_process_timestamp']

    return '''
           user_id is: {}
           user_action is: {}
           last_process_timestamp is: {}
           '''.format(user_id, user_action, last_process_timestamp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  #run app in debug mode on port 5000
    
    