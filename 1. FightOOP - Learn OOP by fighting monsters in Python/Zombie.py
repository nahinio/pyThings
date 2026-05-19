# ============================================================
# Zombie.py
# OOP Concepts: INHERITANCE, CONSTRUCTORS, SELF vs SUPER,
#               POLYMORPHISM
# ============================================================
# Zombie INHERITS from Enemy, meaning it automatically gets
# all of Enemy's attributes and methods for free. It then
# customizes a few of them to feel like a real zombie.
# ============================================================

from Enemy import *   # bring in the Enemy base class
import random         # needed for the 50/50 heal chance

class Zombie(Enemy):  # <-- "Zombie inherits from Enemy"

    # CONSTRUCTOR + SUPER
    # When Python sees Zombie(10, 1) it runs this __init__.
    # We only need healthPoints and attackDamage from the caller
    # because the type is always 'Zombie'. We hard-code that
    # and hand everything up to Enemy's constructor using super().
    #
    # super() refers to the PARENT class (Enemy).
    # self  refers to the current INSTANCE of Zombie.
    # Using super().__init__() lets the parent do its own setup
    # (storing __typeOfEnemy, healthPoints, attackDamage) so we
    # don't have to copy that logic here.
    def __init__(self, healthPoints, attackDamage):
        super().__init__(typeOfEnemy='Zombie',
                         healthPoints=healthPoints,
                         attackDamage=attackDamage)

    # POLYMORPHISM: talk() exists in Enemy, but Zombie has its
    # own version. When Python calls zombie.talk() it uses THIS
    # version, not the parent's. Same method name, different behavior.
    def talk(self):
        print('**Grumbling..**')

    # A Zombie-only method that has no equivalent in Enemy.
    # This is extra behavior added specifically to this subclass.
    def spreadDisease(self):
        print('The Zombie is trying to spread infection')

    # POLYMORPHISM again: specialAttack() in Enemy just prints a
    # fallback message. Here we override it with real logic.
    # There is a 50% chance the zombie heals itself by 2 HP,
    # keeping it alive longer and making the fight unpredictable.
    def specialAttack(self):
        didSpecialAttackSucceed = random.random() < 0.5   # True roughly half the time
        if didSpecialAttackSucceed:
            self.healthPoints += 2                         # self = this zombie instance
            print('The Zombie has healed itself for 2 health points!')
