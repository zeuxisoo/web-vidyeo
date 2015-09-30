from flask.ext.script import Manager, Server
from vidyeo.app import create_app

manager = Manager(create_app())
manager.add_command('runserver', Server())

if __name__ == "__main__":
    manager.run()
