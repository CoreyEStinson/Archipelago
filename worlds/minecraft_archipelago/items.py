from typing import Dict, NamedTuple
from BaseClasses import ItemClassification


class ItemData(NamedTuple):
    code: int
    classification: ItemClassification


PROGRESSIVE_ITEM_BASE_ID = 10000
ITEM_UNLOCK_BASE_ID = 11000
BLOCK_UNLOCK_BASE_ID = 12000
GAMERULE_BASE_ID = 13000
FILLER_ITEM_BASE_ID = 14000

# ── Progressive unlock items ───────────────────────────────────────────────
# Sent multiple times. The mod tracks receipt count and applies the
# matching stage tier (stone → gold → iron → diamond → netherite).
# ──────────────────────────────────────────────────────────────────────────

progressive_items: Dict[str, ItemData] = {
    "Progressive Tools":         ItemData(10000, ItemClassification.progression),
    "Progressive Armor":         ItemData(10001, ItemClassification.progression),
    "Progressive Tools (Gift)":  ItemData(10002, ItemClassification.useful),
    "Progressive Armor (Gift)":  ItemData(10003, ItemClassification.useful),
}

PROGRESSIVE_ITEM_COUNTS = {
    "Progressive Tools":         5,  # stone, gold, iron, diamond, netherite
    "Progressive Armor":         6,  # leather, gold, chainmail, iron, diamond, netherite
    "Progressive Tools (Gift)":  6,  # wooden, stone, gold, iron, diamond, netherite
    "Progressive Armor (Gift)":  6,  # leather, gold, chainmail, iron, diamond, netherite
}

# ── Individual unlock items ────────────────────────────────────────────────
# Each sent once. Unlocks the ability to USE that item type.
# Items marked with (Gift) in filler are the physical give version.
# ──────────────────────────────────────────────────────────────────────────

unlock_items: Dict[str, ItemData] = {
    "Golden Apple":     ItemData(11000, ItemClassification.progression),
    "Bone Meal":        ItemData(11001, ItemClassification.useful),
    "Elytra":           ItemData(11002, ItemClassification.useful),
    "Map":              ItemData(11003, ItemClassification.filler),
    "Shears":           ItemData(11004, ItemClassification.progression),
    "Mace":             ItemData(11005, ItemClassification.progression),
    "Bucket":           ItemData(11006, ItemClassification.progression),
    "Name Tag":         ItemData(11007, ItemClassification.filler),
    "Ominous Bottle":   ItemData(11008, ItemClassification.useful),
    "Potion":           ItemData(11009, ItemClassification.progression),
    "Shield":           ItemData(11010, ItemClassification.progression),
    "Spyglass":         ItemData(11011, ItemClassification.progression),
    "Totem of Undying": ItemData(11012, ItemClassification.useful),
    "Turtle Shell":     ItemData(11013, ItemClassification.useful),
    "Flint and Steel":  ItemData(11014, ItemClassification.progression),
    "Trident":          ItemData(11015, ItemClassification.progression),
    "Bow":              ItemData(11016, ItemClassification.progression),
    "Fishing Rod":      ItemData(11017, ItemClassification.progression),
    "Boat":             ItemData(11018, ItemClassification.progression),
    "Crossbow":         ItemData(11019, ItemClassification.progression),
    "Ender Pearl":      ItemData(11020, ItemClassification.progression),
    "Eye of Ender":     ItemData(11021, ItemClassification.progression),

    # ── Block/structure unlock items ──────────────────────────────────────────
    "Beacon":          ItemData(12000, ItemClassification.progression),
    "Conduit":         ItemData(12001, ItemClassification.progression),
    "Bed":             ItemData(12002, ItemClassification.progression),
    "Furnace":         ItemData(12003, ItemClassification.progression),
    "Anvil":           ItemData(12004, ItemClassification.progression),
    "Brewing Stand":   ItemData(12005, ItemClassification.progression),
    "Ender Chest":     ItemData(12006, ItemClassification.useful),
    "Shulker Box":     ItemData(12007, ItemClassification.useful),
    "Lightning Rod":   ItemData(12008, ItemClassification.progression),
    "Composter":       ItemData(12009, ItemClassification.useful),
    "Smithing Table":  ItemData(12010, ItemClassification.progression),
    "Grindstone":      ItemData(12011, ItemClassification.useful),
    "Torch":           ItemData(12012, ItemClassification.useful),
    "Campfire":        ItemData(12013, ItemClassification.useful),
    "Target":          ItemData(12014, ItemClassification.progression),
    "TNT":             ItemData(12015, ItemClassification.useful),
}



# ── Gamerule items ─────────────────────────────────────────────────────────
# Each permanently changes a world rule when received.
# Comments show the 1.21.1 camelCase gamerule name and the value set on receipt.
# ──────────────────────────────────────────────────────────────────────────

gamerule_items: Dict[str, ItemData] = {
    "Raids":                   ItemData(13000, ItemClassification.progression),
    "Disable Mob Griefing":    ItemData(13001, ItemClassification.useful),
    "No Fall Damage":          ItemData(13002, ItemClassification.useful),
    "No Fire Damage":          ItemData(13003, ItemClassification.useful),
    "No Freeze Damage":        ItemData(13004, ItemClassification.useful),
    "Keep Inventory":          ItemData(13005, ItemClassification.useful),
    "Wandering Traders":       ItemData(13006, ItemClassification.useful),
    "Water Source Conversion": ItemData(13007, ItemClassification.useful),
    "Lava Source Conversion":  ItemData(13008, ItemClassification.useful),
    "Phantom Spawning":        ItemData(13009, ItemClassification.progression),
    "Warden Spawning":         ItemData(13010, ItemClassification.progression),
}

# ── Filler items ───────────────────────────────────────────────────────────
# Physically given to the player on receipt.
# Items that are also in unlock_items above use the (Gift) suffix here.
# ──────────────────────────────────────────────────────────────────────────

filler_items: Dict[str, ItemData] = {

    # — Food Tier 1 ————————————————————————————————————————————————————————
    "Beetroot (Gift)":            ItemData(14000, ItemClassification.filler),
    "Dried Kelp (Gift)":          ItemData(14001, ItemClassification.filler),
    "Potato (Gift)":              ItemData(14002, ItemClassification.filler),
    "Pufferfish (Gift)":          ItemData(14003, ItemClassification.filler),
    "Tropical Fish (Gift)":       ItemData(14004, ItemClassification.filler),
    "Cookie (Gift)":              ItemData(14005, ItemClassification.filler),
    "Glow Berries (Gift)":        ItemData(14006, ItemClassification.filler),
    "Melon Slice (Gift)":         ItemData(14007, ItemClassification.filler),
    "Poisonous Potato (Gift)":    ItemData(14008, ItemClassification.filler),
    "Spider Eye (Gift)":          ItemData(14009, ItemClassification.filler),
    "Rotten Flesh (Gift)":        ItemData(14010, ItemClassification.filler),

    # — Food Tier 2 ————————————————————————————————————————————————————————
    "Raw Chicken (Gift)":         ItemData(14011, ItemClassification.filler),
    "Raw Mutton (Gift)":          ItemData(14012, ItemClassification.filler),
    "Raw Beef (Gift)":            ItemData(14013, ItemClassification.filler),
    "Raw Porkchop (Gift)":        ItemData(14014, ItemClassification.filler),
    "Raw Rabbit (Gift)":          ItemData(14015, ItemClassification.filler),
    "Bread (Gift)":               ItemData(14016, ItemClassification.filler),
    "Rabbit Stew (Gift)":         ItemData(14017, ItemClassification.filler),
    "Apple (Gift)":               ItemData(14018, ItemClassification.filler),

    # — Food Tier 3 ————————————————————————————————————————————————————————
    "Cooked Porkchop (Gift)":     ItemData(14019, ItemClassification.filler),
    "Steak (Gift)":               ItemData(14020, ItemClassification.filler),
    "Pumpkin Pie (Gift)":         ItemData(14021, ItemClassification.filler),
    "Golden Carrot (Gift)":       ItemData(14022, ItemClassification.filler),

    # — Weapons to give ————————————————————————————————————————————————————
    "Trident (Gift)":      ItemData(14023, ItemClassification.filler),
    "Mace (Gift)":         ItemData(14024, ItemClassification.filler),
    "Bow (Gift)":          ItemData(14025, ItemClassification.filler),
    "Crossbow (Gift)":     ItemData(14026, ItemClassification.filler),
    "Arrow (Gift)":        ItemData(14027, ItemClassification.filler),
    "Shield (Gift)":       ItemData(14028, ItemClassification.filler),

    # — Blocks ————————————————————————————————————————————————————————————
    "Cobblestone (Gift)":         ItemData(14029, ItemClassification.filler),
    "Oak Planks (Gift)":          ItemData(14030, ItemClassification.filler),
    "Dirt (Gift)":                ItemData(14031, ItemClassification.filler),
    "Torch (Gift)":               ItemData(14032, ItemClassification.filler),
    "Scaffolding (Gift)":         ItemData(14033, ItemClassification.filler),

    # — Materials ——————————————————————————————————————————————————————————
    "Coal (Gift)":                ItemData(14034, ItemClassification.filler),
    "Iron Ingot (Gift)":          ItemData(14035, ItemClassification.filler),
    "Copper Ingot (Gift)":        ItemData(14036, ItemClassification.filler),
    "Gold Ingot (Gift)":          ItemData(14037, ItemClassification.filler),
    "Emerald (Gift)":             ItemData(14038, ItemClassification.filler),
    "Lapis Lazuli (Gift)":        ItemData(14039, ItemClassification.filler),
    "Redstone (Gift)":            ItemData(14040, ItemClassification.filler),
    "Glowstone Dust (Gift)":      ItemData(14041, ItemClassification.filler),
    "Amethyst Shard (Gift)":      ItemData(14042, ItemClassification.filler),
    "Diamond (Gift)":             ItemData(14043, ItemClassification.filler),
    "Netherite Scrap (Gift)":     ItemData(14044, ItemClassification.filler),
    "Nether Quartz (Gift)":       ItemData(14045, ItemClassification.filler),
    "Leather (Gift)":             ItemData(14046, ItemClassification.filler),

    # — Utility ————————————————————————————————————————————————————————————
    "Bucket (Gift)":          ItemData(14047, ItemClassification.filler),
    "Compass (Gift)":                ItemData(14048, ItemClassification.filler),
    "Fishing Rod (Gift)":     ItemData(14049, ItemClassification.filler),
    "Flint and Steel (Gift)": ItemData(14050, ItemClassification.filler),
    "Boat (Gift)":            ItemData(14051, ItemClassification.filler),
    "Spyglass (Gift)":        ItemData(14052, ItemClassification.filler),

    # — Junk ———————————————————————————————————————————————————————————————
    "Flower (Gift)":              ItemData(14053, ItemClassification.filler),
    "Coral (Gift)":               ItemData(14054, ItemClassification.filler),
    "Painting (Gift)":            ItemData(14055, ItemClassification.filler),
    "Ink Sac (Gift)":             ItemData(14056, ItemClassification.filler),
    "Dye (Gift)":                 ItemData(14057, ItemClassification.filler),
    "Curse Enchanted Book (Gift)": ItemData(14058, ItemClassification.filler),
}

# ── Combined table ─────────────────────────────────────────────────────────

item_table: Dict[str, ItemData] = {
    **progressive_items,
    **unlock_items,
    **gamerule_items,
    **filler_items,
}
