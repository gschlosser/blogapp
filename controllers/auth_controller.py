from flask import Blueprint, request

auth_blueprint = Blueprint('auth_api', __name__)


#login route
@auth_blueprint.route('/login', methods=['POST'])
def login():
    #to log a user in and return auth token
    #body: { username : password}
    #RETURN: {auth_token}
    body = request.json
    print(body["email"], body['password'])
    return {
        "auth_token" : "ldfsdffds21323"
    }


#logout route
@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    return 'logout hit'



#register route
@auth_blueprint.route('/register', methods=['POST'])
def register():
    return 'register hit'
