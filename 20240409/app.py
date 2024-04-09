from flask import Flask, render_template, request, send_file
import routes

app = Flask(__name__)

app.add_url_rule('/', view_func=routes.index)
app.add_url_rule('/plot_graph', view_func=routes.plot_graph, methods=["POST"])
    
if __name__ == '__main__':
    app.run(debug=True)