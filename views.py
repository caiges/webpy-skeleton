import os
import web
from web.contrib.template import render_mako

# hook up mako, override the render function
render = render_mako(
        directories = [os.path.join(os.path.dirname(__file__), 'templates')],
        input_encoding = 'utf-8',
        output_encoding = 'utf-8',
        )

class Home:

    def GET(self, name):
        return render.index(name = name)