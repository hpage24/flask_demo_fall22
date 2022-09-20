#app.py 

from flask import Flask, render_template
app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/addTodo', method=['POST'])
def addTodo():
    #access body information


if __name__ == "__main__":
    app.run(debug=True)
    



#All 4 of them pass information through query parameters and path parameters
# querey parameters www.google.com?page=3&row=34543&user=joe
# path parameters www.google.com/someRootURL/3/34543/joe

#POST and PUT
#Info will be passed in the body -> www.google.com

#GET, PUT, POST, DELETE
#GET and DELETE 


#CRUD CREATE, RETRIEVE, UPDATE, DELETE