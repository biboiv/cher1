import random
import string
import cherrypy

class App2(object):
    @cherrypy.expose
    def index(self):
        return "Hello"
    @cherrypy.expose
    def gen(self):
        return ''.join(random.sample(string.hexdigits,8))
    
if __name__ == '__main__':
    cherrypy.quickstart(App2())
