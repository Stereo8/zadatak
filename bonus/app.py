from flask import Flask
from view.letovi_view import letovi
from view.karte_view import karte

app = Flask(__name__)


app.register_blueprint(letovi)
app.register_blueprint(karte)
app.debug = True

if __name__ == '__main__':
    app.run()
