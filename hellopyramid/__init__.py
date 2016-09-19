from pyramid.config import Configurator
from hellopyramid.resources import Root
import os
import json

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    template = 'hellopyramid:templates/mytemplate.pt'
    config = Configurator(root_factory=Root, settings=settings)
    config.include('pyramid_chameleon')
    config.add_view('hellopyramid.views.my_view',
                    context='hellopyramid:resources.Root',
                    renderer=template)
    config.add_static_view('static', 'hellopyramid:static')
    return config.make_wsgi_app()

