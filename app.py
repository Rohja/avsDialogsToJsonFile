from flask import Flask, request
app = Flask(__name__)

import json
import pprint

pp = pprint.PrettyPrinter(indent=2)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/message', methods=['GET', 'POST'])
def add_message():
    content = request.get_json(silent=True)
    header = content['directive']['header']
    if header['name'] == 'RenderTemplate' and header['namespace'] == 'TemplateRuntime':
        pp.pprint(content)
        with open('avs-dialog.json', 'w') as f:
            f.write(json.dumps(content))
    else:
        print "Message with namespace = '%s' and name = '%s' ignored." % (header['namespace'], header['name'])
    return 'OK'
