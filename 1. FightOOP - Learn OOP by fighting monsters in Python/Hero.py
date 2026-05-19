# ============================================================
# Hero.py
# OOP Concepts: COMPOSITION, CONSTRUCTORS, ENCAPSULATION
# ============================================================
# Hero is a standalone class (no inheritance here).
# It uses COMPOSITION by holding a Weapon object inside it.
# The hero "has a" weapon rather than "being a" weapon.
# ============================================================

from Weapon import *   # we need the Weapon class for the type hint below

class Hero:

    # CONSTRUCTOR (__init__)
    # Sets up the hero's starting stats when you do: Hero(10, 1)
    # Notice Hero does NOT call super() because it has no parent class.
    def __init__(self, healthPoints, attackDamage):
        self.healthPoints = healthPoints    # how much damage the hero can take
        self.attackDamage = attackDamage    # base damage before any weapon
        self.isWeaponEquipped = False       # guard flag so we don't equip twice
        self.weapon: Weapon = None          # COMPOSITION: the hero "has a" Weapon
                                            # slot. It starts empty (None) and gets
                                            # filled in Main.py before the battle.

    # Checks if a weapon is attached and not yet equipped,
    # then adds the weapon's bonus to attackDamage permanently.
    # The isWeaponEquipped flag stops the bonus stacking if
    # equipWeapon() is accidentally called more than once.
    def equipWeapon(self):
        if self.weapon is not None and not self.isWeaponEquipped:
            self.attackDamage += self.weapon.attackIncrease
            self.isWeaponEquipped = True
            print(f'You have equipped a {self.weapon.weaponType} '
                  f'and increased your attack damage by {self.weapon.attackIncrease}!')

    # Prints the hero's attack message with current damage value.
    def attack(self):
        print(f'Hero attacks for {self.attackDamage} damage.')
