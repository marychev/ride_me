class ValidObject:

    @staticmethod
    def road(obj):
        return ValidObject._valid(obj, 'Road')

    @staticmethod
    def rock(obj):
        return ValidObject._valid(obj, 'Rock')

    @staticmethod
    def puddle(obj):
        return ValidObject._valid(obj, 'Puddle')

    @staticmethod
    def lamp(obj):
        return ValidObject._valid(obj, 'Lamp')

    @staticmethod
    def start(obj):
        return ValidObject._valid(obj, 'Start')

    @staticmethod
    def finish(obj):
        return ValidObject._valid(obj, 'Finish')

    @staticmethod
    def bike(obj):
        return ValidObject._valid(obj, 'Bike')

    @staticmethod
    def tools(obj):
        return ValidObject._valid(obj, 'Tools')

    @staticmethod
    def devtools(obj):
        if obj['id'] == 'devtools':
            return obj
        ValidObject.raise_attr(obj, 'devtools')

    @staticmethod
    def background(obj):
        return ValidObject._valid(obj, 'Background')

    @staticmethod
    def scene(obj):
        return ValidObject._valid(obj, 'Scene')

    @staticmethod
    def screen(obj):
        return ValidObject._valid(obj, 'GameScreen')

    @staticmethod
    def menu_screen(obj):
        return ValidObject._valid(obj, 'MenuScreen')

    @staticmethod
    def bikes_screen(obj):
        return ValidObject._valid(obj, 'BikesScreen')

    @staticmethod
    def maps_screen(obj):
        return ValidObject._valid(obj, 'MapsScreen')

    @staticmethod
    def shop_screen(obj):
        return ValidObject._valid(obj, 'ShopScreen')

    @staticmethod
    def _valid(widget, class_name):
        if widget.__class__.__name__ == class_name:
            return widget
        else:
            ValidObject.raise_attr(widget, class_name)

    @staticmethod
    def raise_attr(obj, expected_name):
        raise AttributeError(obj.__class__.__name__, 'is not {}'.format(expected_name))
