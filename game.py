import random

Matrix = [[0 for x in range(5)] for x in range(5)]
Matrix[1][0] = "Dragon"
Matrix[1][1] = 10
Matrix[2][0] = "Vampire"
Matrix[2][1] = 5
Matrix[3][0] = "Cat"
Matrix[3][1] = 1
Weapon = [[0 for x in range(5)] for x in range(5)]

Weapon[1][0] = "Gun"
Weapon[1][1] = 5
Weapon[2][0] = "Flame Thrower"
Weapon[2][1] = 10
Weapon[3][0] = "Stick"
Weapon[3][1] = 1
Weapon[4][0] = "Spit"
Weapon[4][1] = 0

level_amount = 0


def room():
    global level_amount
    random_num = random.randrange(1, 4)
    enemy = Matrix[random_num][0]
    damage_needed = Matrix[random_num][1]
    print '%s has appeared and you are in danger' % (enemy,)
    input_selected = input("Select an action 1 = Gun, 2 = Flame Thrower, 3 = Stick, 4 = Spit")
    weapon_selected = Weapon[input_selected][0]
    damage_weapon = Weapon[input_selected][1]
    if damage_weapon >= damage_needed:
        level_amount += 1
        print "You won, well Done, progress to next level"
        room()
    else:
        if random_num == 1:
            print "The dragon eats you"
        if random_num == 2:
            print "The vampire has sucked your blood"
        if random_num == 3:
            print "You are a nice person, no one should kill a cat"
        print 'your score is : %d' % (level_amount,)
        end_input = input("Game Over, enter 1 to start again")

        if end_input == 1:
            room()
    exit()


room()
