VALID_KEYS = [
    (note, mode)
    for note in [
        "A",
        "A#",
        "Ab",
        "B",
        "Bb",
        "C",
        "C#",
        "Cb",
        "D",
        "D#",
        "Db",
        "E",
        "Eb",
        "F",
        "F#",
        "Fb",
        "G",
        "G#",
        "Gb",
    ]
    for mode in ["major", "minor"]
]

class Key:
    def __init__(self, name: str, mode: str = "major"):
        if (name, mode) not in VALID_KEYS:
            raise ValueError(
                f"Invalid key. Please use a valid key from the list: {format(VALID_KEYS)}"
            )

        self.name = name
        self.mode = mode

    def __str__(self):
        return f"{self.name}{'' if self.mode == 'major' else 'm'}"

    def __repr__(self):
        return f"Key(name='{self.name}', mode='{self.mode}')"

    def __eq__(self, other):
        if isinstance(other, Key):
            return self.name == other.name and self.mode == other.mode
        return False