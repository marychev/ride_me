from kivy.app import App


def get_game_screen():
    app = App.get_running_app()
    if hasattr(app, 'root'):
        return app.root.get_screen('game')
