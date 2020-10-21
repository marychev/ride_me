from kivy.app import App


def get_game_screen():
    app = App.get_running_app()
    return app.root.get_screen('game')
