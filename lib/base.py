import os
from web.contrib.template import render_mako

# Base view for all other views to include (or not).        
class Base:

    # hook up mako, override the render function
    render = render_mako(
            directories = [os.path.join('..', os.path.dirname(__file__), 'templates')],
            input_encoding = 'utf-8',
            output_encoding = 'utf-8',
            )
    