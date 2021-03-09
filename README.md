# IOC Fanger GUI

[![Build Status](https://travis-ci.org/fhightower/ioc-fanger-gui.svg?branch=master)](https://travis-ci.org/fhightower/ioc-fanger-gui)

GUI for fanging and defanging indicators of compromise. This is available at [http://ioc-fanger.hightower.space](http://ioc-fanger.hightower.space).

## Credits

This app was created using Floyd Hightower's Flask template: [https://github.com/fhightower-templates/flask-template](https://github.com/fhightower-templates/flask-template) which allows you to create a Flask app in 30-60 seconds (including Postresql support and potential Heroku deployment). This template uses [cookiecutter](https://github.com/audreyr/cookiecutter) to make it quick, easy, and enjoyable to create projects from templates. If you have not seen either of these projects, you should check them out!

## Quick Start

After cloning the repo...

To create a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for the app, run:

```
make venv
```

Clone the app and run the application at [http://127.0.0.1:5000/](http://127.0.0.1:5000/):

```
make run
```

To test the app, run:

```
make test
```
