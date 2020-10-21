from init import application

@application.route('/')
@application.route('/index')
def index():
    return "Hello world"
