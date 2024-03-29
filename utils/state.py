class State:
    NONE = 'None'
    INIT = 'Init'
    FINISH = 'on_finish'

    EVENT_ON_WAIT = 'on_wait'
    ON_WAIT_START = 'on_wait__start'
    ON_WAIT_MOVE = 'on_wait__move'
    ON_WAIT_STOP = 'on_wait__stop'

    EVENT_ON_JUMP = 'on_jump'
    ON_JUMP_START = 'on_jump__start'
    ON_JUMP_MOVE = 'on_jump__move'
    ON_JUMP_STOP = 'on_jump__stop'

    EVENT_ON_LANDING = 'on_landing'
    ON_LANDING_START = 'on_landing__start'
    ON_LANDING_MOVE = 'on_landing__move'
    ON_LANDING_STOP = 'on_landing__stop'

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
        exclude_events = (
            State.EVENT_ON_JUMP, State.EVENT_ON_LANDING, State.EVENT_ON_RELAX,
            State.EVENT_ON_GO, State.EVENT_ON_STOP, State.EVENT_ON_WAIT)
        return [
            v for v in list(State.__dict__.values())
            if type(v) == str and (v.startswith('on_') or v in (State.NONE, State.INIT)) and v not in exclude_events
        ]
