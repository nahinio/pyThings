# ============================================================
# Main.py
# OOP Concepts: POLYMORPHISM, INHERITANCE, COMPOSITION
# ============================================================
# This file is the entry point of the game. It wires together
# all the classes we built and runs the actual battles.
# Notice how the battle functions work with the Enemy base
# type, not Zombie or Ogre specifically. That is polymorphism
# in action: one function, many possible enemy shapes.
# ============================================================

from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *


# ============================================================
# FUNCTION: Enemybattle
# ============================================================
# Runs a fight between any two Enemy objects.
#
# POLYMORPHISM in the type hint (e1: Enemy, e2: Enemy):
# You can pass a Zombie, an Ogre, or a plain Enemy here and
# the function does not care. It just calls .talk(), .attack(),
# and .specialAttack() and Python figures out which version
# to run based on the real type of the object at runtime.
# ============================================================
def Enemybattle(e1: Enemy, e2: Enemy):

    # Each enemy taunts the other before the fight begins.
    # If e1 is a Zombie, zombie.talk() runs (the overridden one).
    # If e1 is a plain Enemy, Enemy.talk() runs. Same call, different result.
    e1.talk()
    e2.talk()

    # Keep fighting as long as both enemies have health left.
    while e1.healthPoints > 0 and e2.healthPoints > 0:
        print('---------------------------')

        # e2 gets two chances to use its special attack each round.
        # Whether that does anything depends on which class e2 is.
        e2.specialAttack()
        e2.specialAttack()

        # Show current HP so the player can follow along.
        print(f'{e1.getTypeOfEnemy()} has {e1.healthPoints} health points left.')
        print(f'{e2.getTypeOfEnemy()} has {e2.healthPoints} health points left.')

        # Both enemies deal damage to each other.
        e2.attack()
        e1.healthPoints -= e2.attackDamage

        e1.attack()
        e2.healthPoints -= e1.attackDamage

    print('---------------------------')

    # Announce the winner based on who ran out of HP first.
    if e1.healthPoints <= 0:
        print(f'{e1.getTypeOfEnemy()} has been defeated! {e2.getTypeOfEnemy()} wins!')
    elif e2.healthPoints <= 0:
        print(f'{e2.getTypeOfEnemy()} has been defeated! {e1.getTypeOfEnemy()} wins!')


# ============================================================
# FUNCTION: Herobattle
# ============================================================
# Runs a fight between the Hero and any Enemy subclass.
# The hero is NOT an Enemy (no inheritance), so we keep the
# two types separate. COMPOSITION shows up here too: the hero
# carries a Weapon object that already boosted attackDamage
# before this function is even called.
# ============================================================
def Herobattle(h: Hero, e: Enemy):

    # Enemy taunts at the start.
    e.talk()

    # Fight until someone runs out of health.
    while h.healthPoints > 0 and e.healthPoints > 0:
        print('---------------------------')

        # Show current HP for both sides.
        print(f'Hero has {h.healthPoints} health points left.')
        print(f'{e.getTypeOfEnemy()} has {e.healthPoints} health points left.')

        # Enemy gets its special attack chance each round.
        # The exact effect depends on which enemy subclass this is.
        e.specialAttack()

        # Hero attacks the enemy, then enemy attacks back.
        # Damage is applied after both attack() calls so the
        # announcements always print before HP drops.
        h.attack()
        h.healthPoints -= e.attackDamage

        e.attack()
        e.healthPoints -= h.attackDamage

    print('---------------------------')

    # Announce the winner.
    if h.healthPoints <= 0:
        print(f'Hero has been defeated! {e.getTypeOfEnemy()} wins!')
    elif e.healthPoints <= 0:
        print(f'{e.getTypeOfEnemy()} has been defeated! Hero wins!')


# ============================================================
# GAME SETUP
# ============================================================

# Create a Zombie with 10 HP and 1 attack damage.
zombie = Zombie(10, 1)

# Create an Ogre with 20 HP and 3 attack damage.
ogre = Ogre(20, 3)

# Create the Hero with 10 HP and 1 base attack damage.
hero = Hero(10, 1)

# COMPOSITION: create a Weapon and attach it to the Hero.
# The hero object now "has a" weapon stored inside it.
weapon = Weapon('Sword', 6)
hero.weapon = weapon

# equipWeapon() reads hero.weapon and adds its attackIncrease
# to hero.attackDamage. After this, hero.attackDamage = 1 + 6 = 7.
hero.equipWeapon()

# Start the hero vs ogre battle.
# POLYMORPHISM: Herobattle only knows 'e' is an Enemy.
# At runtime it discovers it's an Ogre and calls Ogre's methods.
heroBattle = Herobattle(hero, ogre)
