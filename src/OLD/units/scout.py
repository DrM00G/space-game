from units.unit import Unit

class Scout(Unit):
    def __init__(self, coords, player,unit_number,tech):
        super().__init__(coords, player)
        self.class_type = "E"
        self.strength = 3 + tech[0]
        self.defense = 0 + tech[1]
        self.class_num = 1
        self.speed = 1 + tech[2]
        self.armor = 1
        self.name = 'Scout'
        self.unit_number = unit_number+1
