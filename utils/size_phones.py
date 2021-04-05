class SizePhones:
    redmi_note_8_h = 1080
    redmi_note_8_w = 2340
    redmi_note_8 = (redmi_note_8_h, redmi_note_8_w)

    default = redmi_note_8

    def __init__(self, phone_size: tuple = None) -> None:
        self.current = phone_size or self.default

    @property
    def height(self) -> int:
        return self.current[0]

    @property
    def width(self) -> int:
        return self.current[1]
