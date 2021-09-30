from flask import Flask, request
from caesar import rotate_string
app = Flask('app')

form = """<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>

      <form action = "" method ="POST">
        <label for="rot">Rotate by:</label>
        <input type="text" id="rot" name="rot"></input>
        <label for="text"></label>
        <textarea id="text" name="text" rows="4" cols="50">{0}</textarea>
        <label for="submit"></label>
        <input type="submit"></input>

    </body>
</html>"""


@app.route('/')
def encrypt():
  return form.format("")

@app.route('/',methods=['POST'])
def encrypt_process():
  rot = int(request.form["rot"]) #request syntax?
  text = request.form["text"] # ^^^^
  encrypted = rotate_string(text, rot) #use rot as argument for rotate_string?
  return form.format(encrypted)


app.run(host='0.0.0.0', port=8080)