class ValidObject:

    @staticmethod
    def road(obj):
        if obj.__class__.__name__ == 'Road':
            return obj

    @staticmethod
    def rock(obj):
        if obj.__class__.__name__ == 'Rock':
            return obj

    @staticmethod
    def finish(obj):
        if obj.__class__.__name__ == 'Finish':
            return obj

    @staticmethod
    def bike(obj):
        if obj.__class__.__name__ == 'Bike':
            return obj

    @staticmethod
    def tools(obj):
        if obj.__class__.__name__ == 'Tools':
            return obj
