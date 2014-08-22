import os
from pyramid.paster import get_app
from waitress import serve

port = int(os.environ['PORT'])
application = get_app('development.ini', 'main')
serve(application, host='0.0.0.0', port=port)
