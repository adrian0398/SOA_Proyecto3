from flask import Flask, render_template, request
import requests
from database_service import write

app = Flask(__name__,template_folder='template')
@app.route('/')
def main():
   # main window render
   return render_template('indexIngresar.html')

@app.route("/send/", methods = ['POST', 'GET'])
def sendData():
   # sends data to the dataBase
   if request.form['sending_data'] == "Ingresar datos":
      output = request.form.to_dict()
      
      write(output)
   return render_template('indexIngresar.html')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=9000)
