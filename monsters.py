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
    
Monster('Zombie', 1, 1, 1, 1, .5)
Monster('Skeleton', 2, 2, 1, 1, 1.5)
Monster('Golem', 3, 3, 3, 1, 3)
Monster('Ogre', 3, 2, 2, 2, 2.5)
Monster('Gnome', 4, 1, 4, 4, 3.5)
Monster()
