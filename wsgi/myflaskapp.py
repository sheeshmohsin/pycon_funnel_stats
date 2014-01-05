import flask
import subprocess
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
import jinja2

app = flask.Flask(__name__)

@app.route('/')
def index():
    def inner():
        proc = subprocess.Popen(
            ['python project1.py'],             #call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE
        )

        for line in iter(proc.stdout.readline,''):
            yield line.rstrip() + '<br/>\n'

    env = Environment(loader=FileSystemLoader('templates'),extensions=['jinja2.ext.loopcontrols'])
    tmpl = env.get_template('project.html')
    return flask.Response(tmpl.generate(project=inner()))

app.run(debug=True, port=5000, host='0.0.0.0')
