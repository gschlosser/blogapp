from flask import Flask
from controllers import auth_blueprint

app = Flask(__name__)

@app.route('/')
def say_hello():   
    return 'hello world'

#import blueprint here
app.register_blueprint(auth_blueprint, url_prefix='/auth')
#Any other routes here

if __name__ == '__main__':
    app.run()