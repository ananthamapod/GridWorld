import os
from maze import Maze
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path='/static')
appContext = app.app_context()


def main():
    height = width = 5
    environment = Maze(height, width)
    environment.generate_maze()
    import pdb; pdb.set_trace()
    print environment



@app.route('/')
def welcome():
    return render_template('home2.html')



@app.route('/new_maze', methods=["GET"])
def maze():
    width = int(request.args.get("height"))
    height = int(request.args.get("width"))
    if width and height:
        environment = Maze(height, width)
        environment.generate_maze()
        return jsonify({'maze' : environment._jsonify()})



@app.route('/new', methods=["GET"])
def generate_maze():
    width = int(request.args.get("height"))
    height = int(request.args.get("width"))
    if width and height:
        environment = Maze(height, width)
        environment.generate_maze()
        return render_template('maze.html',
        maze=environment.cells,
        width=environment.width,
        height=environment.height)



port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port), debug=True)
