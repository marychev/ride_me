class Log:
    @staticmethod
    def make_description(title, widget):
        args = (title, widget.current_event, widget.pre_event,
                widget.speed, widget.acceleration, widget.x, widget.y)
        return '{} => {}, (pre: {}). Speed: {}| Acceleration: {}' \
               '\n\tx/y = {} / {}'.format(*args)

    @staticmethod
    def start(name_action, widget):
        title = name_action.upper()
        print('\n{} & {}, (pre: {})'.format(
            title, widget.current_event, widget.pre_event))

    @staticmethod
    def can_or_not(name_action, can, widget):
        title = name_action
        description = Log.make_description(title, widget)
        message = '- Cancel {}\n'.format(description) if not can else '. Can {}'.format(description)
        print(message)

    @staticmethod
    def try_to_set(name_action, widget):
        title = name_action
        message = '.. try set {} => {}(pre: {}).'.format(
            title, widget.current_event, widget.pre_event)
        print(message)
