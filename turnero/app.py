from flask import Flask
from controladores.medicos_controller import medicos_bp
from controladores.pacientes_controller import pacientes_bp
# creo los bp de medicos y pacientes por ahora
app = Flask(__name__)

# Registrar Blueprints 
app.register_blueprint(medicos_bp, url_prefix='/medicos')
app.register_blueprint(pacientes_bp, url_prefix='/pacientes')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
