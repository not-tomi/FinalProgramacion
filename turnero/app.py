from flask import Flask
from controladores.medicos_controller import medicos_blueprint
from controladores.pacientes_controller import pacientes_blueprint
from controladores.turnos_controller import turnos_bp
from controladores.agenda_controller import agenda_bp
# creo los bp 
app = Flask(__name__)

# Registrar Blueprints 
app.register_blueprint(medicos_blueprint, url_prefix='/medicos')
app.register_blueprint(pacientes_blueprint, url_prefix='/pacientes')
app.register_blueprint(turnos_bp, url_prefix='/turnos')
app.register_blueprint(agenda_bp, url_prefix='/agenda')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
