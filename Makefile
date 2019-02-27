clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log* && rm -fr .cache && rm -rf .pytest_cache

venv:
	virtualenv -p python3 ~/.virtualenvs/ioc_fanger_gui && . ~/.virtualenvs/ioc_fanger_gui/bin/activate && pip3 install -r requirements.txt

run:
	~/.virtualenvs/ioc_fanger_gui/bin/python ioc_fanger_gui/ioc_fanger_gui.py

test: clean
	~/.virtualenvs/ioc_fanger_gui/bin/python -m pytest

destroy:
	rm -rf ~/.virtualenvs/ioc_fanger_gui

init:
	. ~/.virtualenvs/ioc_fanger_gui/bin/activate && ~/.virtualenvs/ioc_fanger_gui/bin/python ioc_fanger_gui/manage.py db init

mg:
	~/.virtualenvs/ioc_fanger_gui/bin/python ioc_fanger_gui/manage.py db migrate

up:
	~/.virtualenvs/ioc_fanger_gui/bin/python ioc_fanger_gui/manage.py db upgrade
