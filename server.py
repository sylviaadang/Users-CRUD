from flask_app import app


#  IMPORT CONTROLLERS INTO SERVER
from flask_app.controllers import user_controller

if __name__ == '__main__':
    app.run(debug=True)
