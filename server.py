from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)
app.secret_key = 'happy'

@app.route('/')
def falseStart():
    return redirect('/users')


# This route shows the list of users (read)
@app.route('/users')
def all_users():
    all_users = User.get_all()
    return render_template('read.html', all_users=all_users)

# This route will add the user and then it will show the list of users (create)
@app.route('/users/create', methods=['POST'])
def show():
    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email']
    }

    User.add_user(data)
    return redirect('/users')

# show the created users route
@app.route('/users/new')
def new():
    return render_template('create.html')


# update route
# @app.route('/edit')
# def show_edit_form():

#     return render_template('edit_form.html')



if __name__ == '__main__':
    app.run(debug=True)
