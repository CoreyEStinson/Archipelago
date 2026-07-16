from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import MinecraftArchipelagoWorld


def set_rules(world: "MinecraftArchipelagoWorld") -> None:
    player = world.player
    mw = world.multiworld

    # Shorthand helpers
    def has(item: str, count: int = 1):
        return lambda state: state.has(item, player, count)
    
    def has_any(*items: str):
        return lambda state: any(state.has(i, player) for i in items)
    
    def has_all(*items: str):
        return lambda state: all(state.has(i, player) for i in items)
    
    def tools(tier: int):
        """tier 1=stone, 2=iron, 3=diamond, 4=netherite"""
        return lambda state: state.has("Progressive Tools", player, tier)
    
    def armor(tier: int):
        """tier 1=leather, 2=iron, 3=diamond, 4=netherite"""
        return lambda state: state.has("Progressive Armor", player, tier)
    
    # ── Region entrance rules ─────────────────────────────────────────────
    # These are the most important — they stop the generator softlocking
    # by hiding required items behind regions you can't access yet.

    # Entering the Nether requires lighting a portal with Flint and Steel
    mw.get_entrance("Overworld -> Nether", player).access_rule = \
        has("Flint and Steel")
    
    # Reaching the End requires Eyes of Ender
    mw.get_entrance("Nether -> The End", player).access_rule = \
        has("Eye of Ender")
    
    # Helper
    def rule(location: str, *conditions) -> None:
        if not conditions:
            return
        elif len(conditions) == 1:
            combined = conditions[0]
        else:
            def combined(state):
                return all(cond(state) for cond in conditions)
        set_rule(mw.get_location(location, player), combined)


    # ── Story ─────────────────────────────────────────────────────────────
    # Need buckets to get lava bucket
    rule("Hot Stuff",              has("Bucket"))

    # Building a nether portal requires Flint and Steel to ignite it
    rule("We Need to Go Deeper",   has("Flint and Steel"))

    # Curing a zombie villager requires using a weakness potion and a golden apple
    rule("Zombie Doctor",          has_all("Golden Apple", "Potion"))

    # Need eyes of ender to find stronghold and to enter the End
    # Technically possible without, but not practical (requires a lot of luck)
    rule("Eye Spy",               has("Eye of Ender"))
    rule("The End?",             has("Eye of Ender"))

    # ── Nether (already gated by region, adding extra requirements) ───────

    # Full netherite armor set - need smithing table to upgrade armor
    rule("Cover Me in Debris",      has("Smithing Table"))

    rule("Local Brewery",           has("Brewing Stand"))
    rule("Bring Home the Beacon",   has("Beacon"))
    rule("Beaconator",              has("Beacon"))

    # Potion advancements require being able to use potions
    rule("A Furious Cocktail",     has("Potion"))

    # Need all of the following:
    # - Beacon -> Haste
    # - Conduit -> Conduit Power
    # - Potion -> effects from potions
    # - Ominous Bottle -> Bad Omen, Raid Omen, Trial Omen
    # - Warden Spawning -> Darkness
    rule("How Did We Get Here?",   has_all("Beacon", "Conduit", "Ominous Bottle", "Potion", "Warden Spawning"))
    
    # ── No extra rules for any end advancements ──────────────────────────

    # ── Adventure ─────────────────────────────────────────────────────────

    # Shield deflect
    rule("Not Today, Thank You",   has("Shield"))

    # Spyglass advancements
    rule("Is It a Bird?",       has("Spyglass"))
    rule("Is It a Balloon?",    has_all("Spyglass", "Flint and Steel"))
    rule("Is It a Plane?",      has_all("Spyglass", "Eye of Ender"))

    # Smithing advancements
    # Smithing with style needs end access for spire trim
    rule("Crafting a New Look", has("Smithing Table"))
    rule("Smithing with Style", has("Smithing Table", "Eye of Ender"))

    # Crossbow advancements
    rule("Ol' Betsy",               has("Crossbow"))
    rule("Two Birds, One Arrow",    has_all("Crossbow", "Phantom Spawning"))
    rule("Who's the Pillager Now?", has("Crossbow"))
    rule("Arbalistic",              has("Crossbow"))

    # Can be done with either bow or crossbow
    rule("Take Aim",               has_any("Bow", "Crossbow"))
    rule("Sniper Duel",            has_any("Bow", "Crossbow"))
    rule("Bullseye",               has_any("Bow", "Crossbow"))

    # Trident advancements
    rule("A Throwaway Joke",       has("Trident"))
    rule("Very Very Frightening",  has("Trident")) 
    rule("Surge Protector",        has_all("Trident", "Lightning Rod"))

    # Need beds to sleep
    rule("Sweet Dreams",           has("Bed"))
    
    # Advancements requiring nether:
    # - Country lode take me home -> lodestone (or netherite ingot)
    # - Power of books -> need quartz to craft comparator
    rule("Country Lode, Take Me Home", has("Flint and Steel"))
    rule("The Power of Books", has("Flint and Steel"))

    # Need shears to carve pumpkin for summoning iron golem
    rule("Hired Help",             has("Shears"))

    # Leather boots needed to walk on powder snow
    rule("Light as a Rabbit",      armor(1))
    
    # Totem of Undying
    rule("Postmortal",             has("Totem of Undying"))

    # Raids must be enabled to trigger and win a raid
    rule("Hero of the Village",    has("Raids"))

    # Ominous bottle needed to create ominous vault
    rule("Revaulting",             has("Ominous Bottle"))

    # Mace smash attack
    rule("Over-Overkill",          has("Mace"))

    # Need end exclusive mobs (ender dragon, shulker)
    rule("Monsters Hunted",        has("Eye of Ender"))

    # ── Husbandry ─────────────────────────────────────────────────────────
    
    # Fishing
    rule("Fishy Business",              has("Fishing Rod"))

    # Bucket related advancements
    rule("Bukkit Bukkit",               has("Bucket"))
    rule("Tactical Fishing",            has("Bucket"))
    rule("The Cutest Predator",         has("Bucket"))

    # Need campfire to safely collect honey
    rule("Bee Our Guest",               has("Campfire"))

    # Get in a boat with a goat
    rule("Whatever Floats Your Goat!",  has("Boat"))

   # Remove wolf armor with shears
    rule("Shear Brilliance",            has("Shears"))

    # Advancements that need nether:
    # - Stay Hydrated -> get dried ghast
    # - With Our Powers Combined -> frogs need to eat magma cubes
    # - Two by Two -> breed hoglins & striders
    # - Serious Dedication -> get netherite ingot & upgrade template
    rule("Stay Hydrated!",              has("Flint and Steel"))
    rule("With Our Powers Combined!",   has("Flint and Steel"))
    rule("Two by Two",                  has("Flint and Steel"))
    rule("Serious Dedication",          has_all("Flint and Steel", "Smithing Table"))

    # Eat all foods - need end to eat chorus fruit
    rule("A Balanced Diet",             has("Eye of Ender"))

    # ── Boss kills ────────────────────────────────────────────────────────────
    # Ender Dragon Kill is already gated by The End region (Eye of Ender)
    rule("Wither Kill",                 has("Flint and Steel"))
    rule("Warden Kill",                 has("Warden Spawning")) 
    # Elder Guardian Kill has no gate