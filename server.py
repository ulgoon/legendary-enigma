from backend import create_app
from backend.config.dev import DevConfig


if __name__ == '__main__':
    app = create_app(DevConfig)

    app.run(**DevConfig.RUN_SETTING)
