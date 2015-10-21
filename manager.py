from flask.ext.script import Manager, Server
from vidyeo.app import create_app

app = create_app()

manager = Manager(app)
manager.add_command('runserver', Server())
manager.add_command('runsslserver', Server(ssl_context='adhoc'))

@manager.command
def runsocketio():
    app.socketio.run(app, host="0.0.0.0")

if __name__ == "__main__":
    manager.run()
