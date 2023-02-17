from flask import Flask

application=Flask(__name__)
new=application

@new.route('/home')
def home():
    return "<h1>Welcome to home changes saved. Home page</h1>"

#@new.route('/home',methods=['POST'])
#def home():
#    ret

if __name__ == '__main__':
    new.run(debug=True)

print(__name__)
