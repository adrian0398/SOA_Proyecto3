from flask import Flask, render_template, request
import requests
from database_service import read

months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

app = Flask(__name__,template_folder='template')
@app.route('/')
def main():
   # main window render
   return render_template('indexSeleccionar.html', months=months_list)

@app.route('/selectMonth/', methods = ['POST', 'GET'])
def tables():
    if request.method == 'POST':
        df = read(request.form['month'])
        monthlyData = df.copy()

        table_list = []
        title_list = []
        print("Tabla del mes")
        print(monthlyData)
        table_list.append(monthlyData.to_html(classes='data'))
        title_list.append("Tabla del mes")
        
        Total = monthlyData['Monto'].sum()
        print("Total de gastos del mes")
        print(Total)

        top3 = monthlyData.groupby("Departamento")["Monto"].sum().nlargest(3).index
        print(top3)
        monthlyData["top3"] = monthlyData["Departamento"].isin(top3)
        monthlyData = monthlyData[monthlyData.top3 != False]
        print("3 departamentos con mas gastos en el mes")
        top3_departments = monthlyData[["Departamento", "Monto"]].copy()
        print(top3_departments)
        table_list.append(top3_departments.to_html(classes='data'))
        title_list.append("3 departamentos con mas gastos en el mes")
        print(monthlyData.columns.values)
        print(title_list)

    return render_template('indexSeleccionar.html', tables=table_list, titles=title_list, total=Total, months=months_list, month_selected=request.form['month'])

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)
