from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # flask uses the string to create an html to display
    return "hello page"

@app.route('/without_html')
def without_html():
    # you can return html-stly, too
    return '<h1 style="background-color:powderblue;">This is a heading</h1>'

@app.route('/with_html')
def with_html():
    #render_template loads an html-file and "returns" the content of the file as string
    return render_template("some_html.html")

# POST, because we send the data somewhere else
@app.route('/push_it_somewhere', methods=["POST"])  
def posting_inputs():
    # GET because we recieve the data from somewhere
    some_name = request.form.get("some_name", "")
    #render_template loads an html-file and "returns" the content of the file as string
    return show_name(some_name)

@app.route('/show/<name>')
def show_name(name):
    # use the route to add parameters
    # http://127.0.0.1:5000/show/juenter
    
    app_name = name.upper()
    
    
    return render_template("names.html", html_name = app_name)
    
if __name__ == '__main__':
    app.run(debug=True)