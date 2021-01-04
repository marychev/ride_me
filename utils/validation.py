class ValidObject:

    @staticmethod
    def road(obj):
        class_name = 'Road'
        if obj.__class__.__name__ == class_name:
            return obj
        ValidObject.raise_attr(obj, class_name)

    @staticmethod
    def rock(obj):
        class_name = 'Rock'
        if obj.__class__.__name__ == class_name:
            return obj
        ValidObject.raise_attr(obj, class_name)

    @staticmethod
    def puddle(obj):
        class_name = 'Puddle'
        if obj.__class__.__name__ == class_name:
            return obj
        ValidObject.raise_attr(obj, class_name)

    @staticmethod
    def lamp(obj):
        class_name = 'Lamp'
        if obj.__class__.__name__ == class_name:
            return obj
        ValidObject.raise_attr(obj, class_name)

    @staticmethod
    def start(obj):
        class_name = 'Start'
        if obj.__class__.__name__ == class_name:
            return obj
        ValidObject.raise_attr(obj, class_name)

    @staticmethod
    def finish(obj):
        class_name = 'Finish'
        if obj.__class__.__name__ == class_name:
            return obj
        ValidObject.raise_attr(obj, class_name)

    @staticmethod
    def bike(obj):
        class_name = 'Bike'
        if obj.__class__.__name__ == class_name:
            return obj
        ValidObject.raise_attr(obj, class_name)

    @staticmethod
    def tools(obj):
        class_name = 'Tools'
        if obj.__class__.__name__ == class_name:
            return obj
        ValidObject.raise_attr(obj, class_name)

    @staticmethod
    def background(obj):
        class_name = 'Background'
        if obj.__class__.__name__ == class_name:
            return obj
        ValidObject.raise_attr(obj, class_name)

    @staticmethod
    def raise_attr(obj, expected_name):
        raise AttributeError(obj.__class__.__name__, 'is not {}'.format(expected_name))
