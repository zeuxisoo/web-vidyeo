from flask import request
from flask.ext.socketio import emit, join_room, leave_room, rooms
from ..app import socketio

namespace = '/socket/stream'

@socketio.on('connect', namespace=namespace)
def connect():
    emit('log', {
        'data': 'connect: {0}'.format('Connected')
    })

@socketio.on('disconnect', namespace=namespace)
def disconnect():
    print('Client disconnected', request.sid)

@socketio.on('message', namespace=namespace)
def message(message):
    emit('log', {
        'data': 'message: {0}'.format(message['data'])
    })

@socketio.on('join channel', namespace=namespace)
def join_channel(message):
    join_room(message['channel'])

    emit('log', {
        'data': 'join channel: {0}'.format(', '.join(rooms()))
    })

@socketio.on('leave channel', namespace=namespace)
def leave_channel(message):
    leave_room(message['channel'])

    emit('log', {
        'data': 'leave channel: {0}'.format(', '.join(rooms()))
    })
