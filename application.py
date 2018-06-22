from flask import Flask


def say_hello():
    return "<h1>something here</h1>"


header_text = '''
    <html>
        <head><title>waninger</title></head>
        <body>
    '''

home_link = '<p><a href="/"Back</a></p>'

footer_text = '''
    </body>
</html>
'''

application = Flask(__name__)

application.add_url_rule('/', 'index', (lambda: header_text + home_link + say_hello() + footer_text))

if __name__ == "__main__":
    application.debug = False
    application.run()
