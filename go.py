import os
import web

from sqlalchemy.orm import scoped_session, sessionmaker

from models import *
from views import *

# hook up sqlalchemy
def load_sqla(handler):
    web.ctx.orm = scoped_session(sessionmaker(bind=engine))
    try:
        return handler()
    except web.HTTPError:
       web.ctx.orm.commit()
       raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()

app = web.application(urls, locals())
app.add_processor(load_sqla)



urls = (
    '/(.*)', 'Home'
)

app = web.application(urls, globals(), autoreload = True)

if __name__ == "__main__" : app.run()