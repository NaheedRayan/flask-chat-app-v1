from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app)

# NO:1 
# first it will render the index.html template
@app.route('/')
def home():
    return render_template("index.html")

# NO:2
# It will get the form data from the index.html and pass it to chat.html
@app.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')

    # if there is data then we wiil render chat.html and pass two arguments
    if username and room:
        return render_template('chat.html', username=username, room=room)
    else:
        return redirect(url_for('home'))

# NO:4
@socketio.on('join_room')
def handle_join_room_event(data):
    # here app.logger is used instead of print because it also prints the time of log.
    app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    # then it will create a room using the join_room function .
    # Then it will call a join_room_announcement event in chat.html and send data
    # and emit the join room announcement in the created room.
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])

# NO:7
@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {}: {}".format(data['username'],
                                                                    data['room'],
                                                                    data['message']))
    socketio.emit('receive_message', data, room=data['room'])



# NO:10
# if someone left the room then we will announce it
@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info("{} has left the room {}".format(data['username'], data['room']))
    leave_room(data['room'])
    socketio.emit('leave_room_announcement', data, room=data['room'])


if __name__ == '__main__':
    # socketio.run(app , debug = True)
    # socketio.run(app,host = "192.168.43.151" , port= 5000, debug=True )
    


    # we are using eventlet
    # it will also work for local device setup
    # here socketio is a wrapper function
    socketio.run(app,host = "0.0.0.0" , port= 5000, debug=True )

    # for heroku if we use gevent in the Procfile
    # app.run()