import redis

def create_app():
    env_config = get_config()

    app = Flask(__name__)

    return app