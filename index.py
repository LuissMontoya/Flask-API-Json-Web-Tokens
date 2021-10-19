from flask import Flask

app =  Flask(__name__)

#Rutes

@app.route('/unprotected')
def unprotected():
    return ''

@app.route('/protected')
def protected():
    return ''


@app.route('/login')
def login():
    return ''



if __name__ == '__main__':
    app.run(debug=True)