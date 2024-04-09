from flask import Flask, render_template, request, send_file
from plotter import plot_function


def index():
    return render_template("index.html")

def plot_graph():
    function_str = request.form.get("function", "")
    print(f"str send: {function_str}")
    try:
        image_file = plot_function(function_str)
        return send_file(image_file, mimetype='image/png')
    except Exception as err:
        return render_template("index.html", error=str(err))
