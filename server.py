from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def start():
	return render_template("index.html", rows=8, cols=8, color1="color1", color2="color2")

@app.route('/<int:rows>')
def startwRows(rows):
	return render_template("index.html", rows=rows, cols=8, color1="color1", color2="color2")

@app.route('/<int:rows>/<int:cols>')
def startwRowsCols(rows,cols):
	return render_template("index.html", rows=rows, cols=cols, color1="color1", color2="color2")

def getColor(color):
  if color == "red":
    return "color1"
  elif color == "black":
    return "color2"
  elif color == "white":
    return "color3"
  elif color == "green":
    return "color4"
  else:
    return color

@app.route('/<int:rows>/<int:cols>/<string:color1>/<string:color2>')
def startwRowsColsColors(rows,cols,color1="color1",color2="color2"):
  color1res = getColor(color1)
  color2res = getColor(color2)
  return render_template("index.html", rows=rows, cols=cols, color1=color1res, color2=color2res)

if __name__=="__main__":
  app.run(debug=True)