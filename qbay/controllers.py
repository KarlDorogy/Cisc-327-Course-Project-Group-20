from flask import render_template, request, session, redirect
from qbay.models import *
from datetime import date

from qbay import app


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object
    Wrap any python function and check the current session to see if
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.
    To wrap a function, we can put a decoration on that function.
    Example:
    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            try:
                user = User.query.filter_by(email=email).one_or_none()
                if user:
                    # if the user exists, call the inner_function
                    # with user as parameter
                    return inner_function(user)
            except Exception:
                pass
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = login(email, password)
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information
        between a user's browser and the end server.
        Typically it is packed and stored in the browser cookies.
        They will be past along between every request the browser made
        to this services. Here we store the user object into the
        session, so we can tell if the client has already login
        in the following sessions.
        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='login failed')


@app.route('/')
@authenticate
def home(user):

    # gets a list of products that the logged in user owns
    user_products = get_products(user.email)
    return render_template('index.html', user=user, products=user_products)


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None

    if password != password2:
        error_message = "The passwords do not match"
    else:
        # use backend api to register the user
        success = register(name, email, password)
        if not success:
            error_message = "Registration Failed."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/updateuser', methods=['Get'])
def update_user_get():
    return render_template('updateuser.html', 
                           message='Please enter new info below:')


@app.route('/updateuser', methods=['POST'])
def update_user_post():

    # retrieves current logged in user's email
    user_email = session['logged_in']

    name = request.form.get('name')
    shipping_address = request.form.get('shippingaddress')
    postal_code = request.form.get('postalcode')
    error_message = None

    # use backend api to update the user attributes
    success = update_user(user_email, name, shipping_address, postal_code)
    if not success:
        error_message = "Updating of User Profile Failed."
    # if there is any error messages when updateing user profile
    # at the backend, go back to the update page.
    if error_message:
        return render_template('updateuser.html', message=error_message)
    else:
        return redirect('/', code=303)


@app.route('/updateproduct', methods=['Get'])
def update_product_get():
    return render_template('updateproduct.html', 
                           message="Please enter new product info below:", 
                           pName=request.args.get('pName'))


@app.route('/updateproduct', methods=['POST'])
def update_product_post():
    new_price = int(request.form.get('new_price'))
    new_title = request.form.get('new_title')
    new_description = request.form.get('new_description')
    title = request.form.get('title')
    # use backend api to update the user attributes
    success = update_product(new_price, new_title, new_description, title)
    error_message = None
    if not success:
        error_message = "Product Update Failed"
    # if there is any error messages when creating a product
    # at the backend, go back to the create product page.
    if error_message:
        return render_template('updateproduct.html', message=error_message, 
                               pName=request.args.get('pName'))
    else:
        return redirect('/', code=303)


@app.route('/createproduct', methods=['Get'])
def create_product_get():
    return render_template('createproduct.html', 
                           message='Please enter product info below:')


@app.route('/createproduct', methods=['POST'])
def create_product_post():
    # retrieves current logged in user's email
    owner_email = session['logged_in']
    today = date.today()
    current_date = today.strftime("%d/%m/%Y")
    last_modified_date = (current_date[6:10] + 
                          "-" + current_date[3:5] + "-" + current_date[0:2])
    price = int(request.form.get('price'))
    title = request.form.get('title')
    description = request.form.get('description')
    error_message = None
    # use backend api to update the user attributes
    success = create_product(price, title, description, 
                             last_modified_date, owner_email)
    if not success:
        error_message = "Product Creation Failed."
    # if there is any error messages when creating a product
    # at the backend, go back to the create product page.
    if error_message:
        return render_template('createproduct.html', message=error_message)
    else:
        return redirect('/', code=303)


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')
