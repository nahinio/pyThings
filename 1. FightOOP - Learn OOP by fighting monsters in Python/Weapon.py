# ============================================================
# Weapon.py
# OOP Concept: COMPOSITION
# ============================================================
# Composition means one class "owns" an object of another class
# as a part of itself. Here, Hero doesn't inherit from Weapon,
# it simply holds a Weapon object inside it. That relationship
# ("has-a" instead of "is-a") is what composition is all about.
# ============================================================

class Weapon:

    # CONSTRUCTOR (__init__)
    # Called automatically the moment you do: Weapon('Sword', 6)
    # It sets up every new Weapon with its own name and attack boost.
    def __init__(self, weaponType, attackIncrease):
        self.weaponType = weaponType          # e.g. 'Sword', 'Axe'
        self.attackIncrease = attackIncrease  # how much damage this weapon adds
