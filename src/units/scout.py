from units.unit import Unit

class Scout(Unit):
    def __init__(self,player,unit_index,p_index,init_coords,turn_bought,tech):
        super().__init__(player,unit_index,p_index,init_coords,turn_bought)
        self.can_move=True
        self.attack = 3 + tech[0]
        self.defense = 1 + tech[1]
        self.tactics = 1
        self.movement = 1 + tech[2]
        self.armor = 2
        self.name = 'Scout'
        self.combat_ready = True

