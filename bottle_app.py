from bottle import route, run, error, static_file, template, TEMPLATE_PATH, debug, default_app
TEMPLATE_PATH.insert(0,'/')



@route('/')
def index():
    return template('index')


def css_callback(filename):
    return static_file(filename, root='./')
route('/<filename>','GET', css_callback)


def img_callback(filename):
    return static_file(filename, root='./my_pipe_collection')
route('/my_pipe_collection/<filename>','GET', img_callback)


def img_call(filename):
    return static_file(filename, root='./my_pipe_collection/Tools')
route('/my_pipe_collection/Tools/<filename>','GET', img_call)



@route('/')
def main_page():
    return static_file("index.html", root='./')


@route('/index.html')
def characters_page():
    return static_file("index.html", root='./')


@route('/effects.html')
def characters_page():
    return static_file("effects.html", root='./')

@route('/observation.html')
def reviews_page():
    return static_file("observation.html", root='./')

@route('/tools.html')
def movies_page():
    return static_file("tools.html", root='./')


def htmlify(title,text):
    page = '''
    !DOCTYPE html>
    <html>
    <head>
        <title>%s</title>
        <meta charset="utf-8" />
    </head>
    <body>
       %s
    </body>
    </html>
    ''' % (title,text)
    return page

@error(404)
def error404(error):
    return '<h1> You have experienced a 404<h1>'
# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

