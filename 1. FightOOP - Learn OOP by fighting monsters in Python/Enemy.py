# ============================================================
# Enemy.py
# OOP Concepts: ABSTRACTION, ENCAPSULATION, CONSTRUCTORS
# ============================================================
# This is the BASE class. Think of it as a blueprint that
# describes what every enemy in the game must have and be
# able to do. Zombie and Ogre will both inherit from this.
# ============================================================

class Enemy:

    # CONSTRUCTOR (__init__)
    # Runs automatically when you create a new Enemy (or any
    # subclass like Zombie/Ogre). It receives the enemy type,
    # health, and attack damage, then stores them on the object.
    def __init__(self, typeOfEnemy, healthPoints, attackDamage):

        # ENCAPSULATION: the double underscore (__) makes
        # __typeOfEnemy a "private" attribute. Code outside
        # this class cannot do enemy.__typeOfEnemy directly.
        # It can only read it through the getter below.
        self.__typeOfEnemy = typeOfEnemy

        # healthPoints and attackDamage are public, so the
        # battle functions in Main.py can read and change them.
        self.healthPoints = healthPoints
        self.attackDamage = attackDamage

    # Prints a taunt when the enemy enters the battle.
    def talk(self):
        print(f'I am a {self.__typeOfEnemy}. Be prepared to fight!')

    # Describes the enemy stepping toward the player.
    def walkForward(self):
        print(f'{self.__typeOfEnemy} moves closer to you.')

    # Prints the basic attack message with current damage value.
    def attack(self):
        print(f'{self.__typeOfEnemy} attacks for {self.attackDamage} damage.')

    # ABSTRACTION: specialAttack acts as a placeholder here.
    # The base Enemy class does not know what the special attack
    # should do, so it just prints a fallback message.
    # Each subclass (Zombie, Ogre) will override this with its
    # own real logic. Hiding those details here is abstraction.
    def specialAttack(self):
        print('Enemy has no special attack!')

    # GETTER METHOD (part of Encapsulation)
    # Because __typeOfEnemy is private, this is the only safe
    # way for outside code to read it. The real data stays
    # protected; we just hand back a copy of the value.
    def getTypeOfEnemy(self):
        return self.__typeOfEnemy
