class Log:
    @staticmethod
    def start(name_action, widget):
        title = name_action.upper()
        print('\n{} & {}, (pre: {})'.format(title, widget.current_event, widget.pre_event))

    @staticmethod
    def can_or_not(name_action, can, widget):
        title = name_action
        if not can:
            print('- Cancel {} => {}, (pre: {})\n'.format(title, widget.current_event, widget.pre_event))
        else:
            print('+ Set {} => {}, (pre: {}). Speed: {}'.format(
                title, widget.current_event, widget.pre_event,
                widget.speed))

    @staticmethod
    def try_to_set(name_action, widget):
        title = name_action
        print('. try set {} => {}, (pre: {}). Speed: {}'.format(
            title, widget.current_event, widget.pre_event,
            widget.speed))
