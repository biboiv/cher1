import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello from CherryPy"

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())
