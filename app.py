from flask import Flask
import views


def create_app():
    temp_app = Flask(__name__)
    temp_app.config["DEBUG"] = True
    temp_app.secret_key = 'secret key'
    temp_app.add_url_rule("/", view_func=views.home_page)
    return temp_app


app = create_app()

if __name__ == "__main__":
    app.run()
