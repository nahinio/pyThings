# ============================================================
# Ogre.py
# OOP Concepts: INHERITANCE, CONSTRUCTORS, SELF vs SUPER,
#               POLYMORPHISM
# ============================================================
# Ogre also inherits from Enemy, just like Zombie does.
# Comparing Zombie and Ogre side by side is a great way to
# see how two sibling classes can share the same parent but
# behave completely differently.
#
# BUG FIXED: in the original code, specialAttack() was
# indented inside talk(), making it a nested function that
# could never be called from outside. It has been moved to
# the correct indentation level as a proper class method.
# ============================================================

from Enemy import *   # bring in the Enemy base class
import random         # needed for the 20% power-up chance

class Ogre(Enemy):    # <-- "Ogre inherits from Enemy"

    # CONSTRUCTOR + SUPER
    # Same pattern as Zombie: the caller only passes health and
    # damage; we hard-code 'Ogre' as the type and let the parent
    # constructor store everything via super().__init__().
    def __init__(self, healthPoints, attackDamage):
        super().__init__(typeOfEnemy='Ogre',
                         healthPoints=healthPoints,
                         attackDamage=attackDamage)

    # POLYMORPHISM: overrides Enemy's talk() with Ogre flavor.
    # The parent version says "I am an Enemy", this one shows
    # the ogre's intimidating behavior instead.
    def talk(self):
        print('Ogre is slamming hands all around')

    # POLYMORPHISM: overrides Enemy's placeholder specialAttack().
    # The ogre has a 20% chance to permanently boost its own
    # attack damage by 4, making it hit harder for the rest of
    # the battle. This is intentionally rarer than the Zombie's
    # heal to give each enemy a unique feel.
    #
    # self.attackDamage refers to the attribute set in Enemy's
    # __init__ via super(). Even though it lives in the parent,
    # self always points to the current Ogre instance so we can
    # read and update it directly here.
    def specialAttack(self):
        didSpecialAttackSucceed = random.random() < 0.2   # True roughly 1 in 5 times
        if didSpecialAttackSucceed:
            self.attackDamage += 4
            print('The Ogre has increased its attack damage by 4 for the next attack!')
