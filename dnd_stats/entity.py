class Entity:
    def __init__(self, name, position):
        self.name = name
        self.initiative = -1
        self.health = 1
        self.position = position
        self.damage_taken = []
        self.damage_dealth = []
        self.history = []
        self.movement = 30

    def set_health(self, health):
        self.health = health

    def set_initiative(self, initiative):
        self.initiative = initiative

    def took_damage(self, damage):
        assert isinstance(damage, int)
        self.damage_taken.append(damage)
        self.health -= damage

    def dealt_damage(self, damage):
        assert isinstance(damage, int)
        self.damage_dealth.append(damage)

    def move(self, newPos):
        pass

    def took_action(self, attack_roll=None, damage_roll=None, damage_taken=None):
        if damage_taken:
            self.history.append({'type': 'hit', 'damage': damage_taken})
        else:
            self.history.append({'type': 'attack', 'damage': damage_roll, 'attack': attack_roll})
