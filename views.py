from lib import Base

class Home(Base):

    def GET(self, name):
        return render.hello(name = name)