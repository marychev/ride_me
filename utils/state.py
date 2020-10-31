class State:
    NONE = 'None'

    EVENT_ON_JUMP = 'on_jump'
    ON_JUMP_START = 'on_jump__start'
    ON_JUMP_LANDING = 'on_jump__landing'
    ON_JUMP_LANDING_STOP = 'on_jump__landing__stop'
    ON_JUMP_UP_MOVE = 'on_jump__up__move'
    ON_JUMP_UP_STOP = 'on_jump__up__stop'

    EVENT_ON_GO = 'on_go'
    ON_GO_START = 'on_go__start'
    ON_GO_MOVE = 'on_go__move'
    ON_GO_STOP = 'on_go__stop'

    EVENT_ON_RELAX = 'on_relax'
    ON_RELAX_START = 'on_relax__start'
    ON_RELAX_MOVE = 'on_relax__move'
    ON_RELAX_STOP = 'on_relax__stop'

    EVENT_ON_STOP = 'on_stop'
    ON_STOP_START = 'on_stop__start'
    ON_STOP_MOVE = 'on_stop__move'
    ON_STOP_STOP = 'on_stop__stop'

    @classmethod
    def list_states(cls):
        exclude_events = (State.EVENT_ON_JUMP, State.EVENT_ON_GO, State.EVENT_ON_RELAX, State.EVENT_ON_STOP)
        return [
            v for v in list(State.__dict__.values())
            if type(v) == str and not v.startswith('__') and v not in exclude_events
        ]
