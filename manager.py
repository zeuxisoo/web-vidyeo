from gevent import monkey
monkey.patch_all()

from flask.ext.script import Manager, Server
from vidyeo.app import create_app, socketio

app = create_app()

manager = Manager(app)
manager.add_command('runserver', Server())
manager.add_command('runsslserver', Server(ssl_context='adhoc'))

@manager.command
def runsocketio():
    socketio.run(app, host="0.0.0.0")

if __name__ == "__main__":
    manager.run()
