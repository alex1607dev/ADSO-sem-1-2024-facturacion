from flask import Flask, render_template   

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_usuarios')
def login_usuarios():
    return render_template('login_usuarios.html')

@app.route('/login_admin')
def login_admin():
    return render_template('login_admin.html')

@app.route('/listar_productos')
def listar_productos():
    return render_template('listar_productos.html')

@app.route('/formulario_producto')
def formulario_producto():
    return render_template('formulario_producto.html')

@app.route('/listar_clientes')
def listar_clientes():
    return render_template('listar_clientes.html')

@app.route('/formulario_clientes')
def formulario_clientes():
    return render_template('formulario_clientes.html')

@app.route('/Listar_usuarios')
def Listar_usuarios():
    return render_template('Listar_usuarios.html')

@app.route('/formulario_usuarios')
def formulario_usuarios():
    return render_template('formulario_usuarios.html')

@app.route('/Listar_facturas')
def Listar_facturas():
    return render_template('Listar_facturas.html')

@app.route('/formulario_factura')
def formulario_facturas():
    return render_template('formulario_factura.html')