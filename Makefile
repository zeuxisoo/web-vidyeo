all:
	@echo "make venv"
	@echo "make server"

venv:
	virtualenv-2.7 --no-site-package venv
	source venv/bin/activate && pip install -r requirements.txt

server:
	source venv/bin/activate && python manager.py runserver

prod-server:
	source venv/bin/activate && python manager.py runserver -h 0.0.0.0 -p 5000

watch:
	npm run watch

assets:
	npm run production
