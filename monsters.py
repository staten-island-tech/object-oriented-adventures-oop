import random
class Monster():
    def __init__(data,monster, monster_level, attack_strength, health_level, speed, experince_dropped ):
        data.monster = monster 
        data.monster_level = monster_level
        data.attack_strength = attack_strength
        data.health_level = health_level
        data.speed = speed
        data.experince_dropped = experince_dropped

    def __str__(data):
        return f"{data.monster},{data.monster_level},{data.attack_strength},{data.health_level},{data.speed},{data.experince_dropped}"
    
def Zombie():
    super