import random
r = random.randrange
class Monster():
    def __init__(data,monster, monster_level, attack_strength, health_level, speed, experince_dropped,money_dropped ):
        data.monster = monster 
        data.monster_level = monster_level
        data.attack_strength = attack_strength
        data.health_level = health_level
        data.speed = speed
        data.experince_dropped = experince_dropped
        data.money_dropped = money_dropped

    def __str__(data):
        return f"{data.monster},{data.monster_level},{data.attack_strength},{data.health_level},{data.speed},{data.experince_dropped}"
    
Monster('Zombie', 1, r(1,2), r(1,2) , r(1,3), r(1,5), r(1,5))
Monster('Skeleton')
Monster('Golem')
Monster('Ogre')
Monster('Gnome')
