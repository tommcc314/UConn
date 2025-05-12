from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Retrieve cookies from the request
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
    q1b1_cookie = request.cookies.get('Q1B1')
    q1b2_cookie = request.cookies.get('Q1B2')
    q1b3_cookie = request.cookies.get('Q1B3')
    
    return render_template('index.html', q1b1_cookie=q1b1_cookie, q1b2_cookie=q1b2_cookie, q1b3_cookie=q1b3_cookie)

@app.route('/set_cookies')
def set_cookies():
    return render_template('set_cookies.html')

@app.route('/set_user_cookies', methods=['POST'])
def set_user_cookies():
    user_choice = request.form['user']

    response = make_response(render_template('set_cookies.html'))

    if user_choice == 'user1':
        response.set_cookie('Q1B1', 'fvg20002')
        response.set_cookie('Q1B2', 'graham', path='/Q1B2')
        response.set_cookie('Q1B3', '172.16.49.88', httponly=True)
    elif user_choice == 'user2':
        response.set_cookie('Q1B1', 'tkm20002')
        response.set_cookie('Q1B2', 'mccarthy', path='/Q1B2')
        response.set_cookie('Q1B3', '172.16.49.96', httponly=True)

    return response

@app.route('/Q1B2')
def display_q1b2_cookie():
    # Display the value of Q1B2 cookie
    # This cookie is sent only for requests to folder Q1B2 of the website
    q1b2_cookie = request.cookies.get('Q1B2')
    return f'Q1B2 Cookie: {q1b2_cookie}'

if __name__ == '__main__':
    app.run(debug=True)
