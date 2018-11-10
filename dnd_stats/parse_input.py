def parse_attack(attack_str):
    # Attack strings should be in [Character] [Roll] [Damage]
    character, roll, damage = attack_str.split()
    return character, int(roll), int(damage)
