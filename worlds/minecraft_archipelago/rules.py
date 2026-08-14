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
        """tier 1=stone, 2=gold, 3=iron, 4=diamond, 5=netherite"""
        return lambda state: state.has("Progressive Tools", player, tier)

    def armor(tier: int):
        """tier 1=leather, 2=gold, 3=chainmail, 4=iron, 5=diamond, 6=netherite"""
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

    # Building a nether portal requires Flint and Steel to ignite it
    rule("We Need to Go Deeper",   has("Flint and Steel"))

    # Curing a zombie villager requires using a golden apple
    rule("Zombie Doctor",          has("Golden Apple"))

    # Cover Me with Diamonds requires diamond armor
    rule("Cover Me with Diamonds", armor(5))

    # ── Adventure ─────────────────────────────────────────────────────────

    # Shield deflect
    rule("Not Today, Thank You",   has("Shield"))

    # Crossbow advancements
    rule("Ol' Betsy",              has("Crossbow"))
    rule("Two Birds, One Arrow",   has("Crossbow"))
    rule("Who's the Pillager Now?", has("Crossbow"))
    rule("Arbalistic",             has("Crossbow"))

    # Can be done with either bow or crossbow
    rule("Bullseye",               has_any("Bow", "Crossbow"))
    rule("Take Aim",               has_any("Bow", "Crossbow"))
    rule("Sniper Duel",            has_any("Bow", "Crossbow"))

    # Trident advancements
    rule("A Throwaway Joke",       has("Trident"))
    rule("Very Very Frightening",  has("Trident")) 

    # Totem of Undying
    rule("Postmortal",             has("Totem of Undying"))

    # Raids must be enabled to trigger and win a raid
    rule("Hero of the Village",    has("Raids"))

    # Potion advancements require being able to use potions
    rule("A Furious Cocktail",     has("Potion"))
    rule("How Did We Get Here?",   has("Potion"))

    # Mace smash attack
    rule("Over-Overkill",          has("Mace"))

    # Ominous bottle needed to create ominous vault
    rule("Revaulting",             has("Ominous Bottle"))

    # Scraping copper needs an axe (any tool tier works)
    rule("Lighten Up",             tools(1))

    # Fishing
    rule("Fishy Business",         has("Fishing Rod"))

    # ── Nether (already gated by region, adding extra requirements) ───────

    # Mining ancient debris needs diamond pickaxe
    rule("Hidden in the Depths",   tools(4))

    # Full netherite armor set — needs diamond tools to mine debris and smithing table to apply netherite
    rule("Cover Me in Debris",     tools(4), has("Smithing Table"))

    # ── Husbandry ─────────────────────────────────────────────────────────

    # Leather boots needed to walk on powder snow
    rule("Light as a Rabbit",      armor(1))

    # ── Boss kills ────────────────────────────────────────────────────────────
    # Ender Dragon Kill is already gated by The End region (Eye of Ender)
    rule("Wither Kill",          has("Flint and Steel"))
    rule("Warden Kill",          has("Warden Spawning"))
    # Elder Guardian Kill has no gate

    rule("Local Brewery",        has("Brewing Stand"))
    rule("Bring Home the Beacon",has("Beacon"))
    rule("Beaconator",           has("Beacon"))