from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route("/")
def main():
  return render_template('index.html')

@app.route("/", methods=['POST'])
def generateQR():
  memory = BytesIO()
  data = request.form.get('link')
  img = qrcode.make(data)
  img.save(memory) # Save to temporary memory
  memory.seek(0) # Set pointer to front of the memory block

  base64_img = "data:image/png;base64," + \
    b64encode(memory.getvalue()).decode("ascii")

  return render_template('index.html', data=base64_img)

if __name__ == '__main__':
  app.run(debug=True)