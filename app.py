from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Use /form"

@app.route("/login")
def login():
    return {"author": "1160491"}

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/size2json", methods=['POST'])
def size2json():
    from PIL import Image
    
    image = request.files['image']
    
    im = Image.open(image)
    if im.format != "PNG":
        return {"result": "invalid filetype"}
    
    result_size = {'width': im.size[0], 'height': im.size[1]}
    
    return result_size

if __name__ == "__main__":
    app.run(debug=True)