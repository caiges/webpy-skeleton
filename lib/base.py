from web.contrib.template import render_mako
        
class Base:

    # hook up mako, override the render function
    render = render_mako(
            directories = [os.path.join('..', os.path.dirname(__file__), 'templates')],
            input_encoding = 'utf-8',
            output_encoding = 'utf-8',
            )
    