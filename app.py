"""
Author: Kanak Sachan
Date: 2024-05-19
Copyright (c) 2024 Kanak Sachan
Description: A basic Flask application using blueprint structure.
"""
from flask import Flask
from flask_jwt_extended import JWTManager
from application import application as application_blueprint

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ'  # Change this to a random secret key
jwt = JWTManager(app)

app.register_blueprint(application_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


