from typing import Dict, NamedTuple
from BaseClasses import ItemClassification


class ItemData(NamedTuple):
    code: int
    classification: ItemClassification


ITEM_BASE_ID = 43000

# ── Progressive unlock items ───────────────────────────────────────────────
# Sent multiple times. The mod tracks receipt count and applies the
# matching stage tier (stone → iron → diamond → netherite).
# ──────────────────────────────────────────────────────────────────────────

progressive_items: Dict[str, ItemData] = {
    "Progressive Tools":  ItemData(43000, ItemClassification.progression),
    "Progressive Armor":  ItemData(43001, ItemClassification.progression),
}

PROGRESSIVE_ITEM_COUNTS = {
    "Progressive Tools": 4,  # stone, iron, diamond, netherite
    "Progressive Armor": 4,  # leather, iron, diamond, netherite
}

# ── Individual unlock items ────────────────────────────────────────────────
# Each sent once. Unlocks the ability to USE that item type.
# Items marked with (Gift) in filler are the physical give version.
# ──────────────────────────────────────────────────────────────────────────

unlock_items: Dict[str, ItemData] = {
    "Golden Apple":     ItemData(43002, ItemClassification.useful),
    "Bone Meal":        ItemData(43003, ItemClassification.useful),
    "Elytra":           ItemData(43004, ItemClassification.useful),
    "Map":              ItemData(43005, ItemClassification.filler),
    "Shears":           ItemData(43006, ItemClassification.useful),
    "Mace":             ItemData(43007, ItemClassification.useful),
    "Bucket":           ItemData(43008, ItemClassification.useful),
    "Name Tag":         ItemData(43009, ItemClassification.filler),
    "Ominous Bottle":   ItemData(43010, ItemClassification.useful),
    "Potion":           ItemData(43011, ItemClassification.useful),
    "Shield":           ItemData(43012, ItemClassification.useful),
    "Spyglass":         ItemData(43013, ItemClassification.useful),
    "Totem of Undying": ItemData(43014, ItemClassification.useful),
    "Turtle Shell":     ItemData(43015, ItemClassification.useful),
    "Flint and Steel":  ItemData(43016, ItemClassification.useful),
    "Trident":          ItemData(43017, ItemClassification.useful),
    "Bow":              ItemData(43018, ItemClassification.useful),
    "Fishing Rod":      ItemData(43019, ItemClassification.useful),
    "Boat":             ItemData(43020, ItemClassification.useful),
    "Crossbow":         ItemData(43021, ItemClassification.useful),
    "Ender Pearl":      ItemData(43022, ItemClassification.progression),
    "Eye of Ender":     ItemData(43023, ItemClassification.progression),
}

# ── Gamerule items ─────────────────────────────────────────────────────────
# Each permanently changes a world rule when received.
# Comments show the 1.21.1 camelCase gamerule name and the value set on receipt.
# ──────────────────────────────────────────────────────────────────────────

gamerule_items: Dict[str, ItemData] = {
    "Raids":                   ItemData(43024, ItemClassification.useful),   # disableRaids false
    "Disable Mob Griefing":    ItemData(43025, ItemClassification.useful),   # mobGriefing false
    "No Fall Damage":          ItemData(43026, ItemClassification.useful),   # fallDamage false
    "No Fire Damage":          ItemData(43027, ItemClassification.useful),   # fireDamage false
    "No Freeze Damage":        ItemData(43028, ItemClassification.useful),   # freezeDamage false
    "Keep Inventory":          ItemData(43029, ItemClassification.useful),   # keepInventory true
    "Wandering Traders":       ItemData(43030, ItemClassification.useful),   # doTraderSpawning true
    "Water Source Conversion": ItemData(43031, ItemClassification.useful),   # waterSourceConversion true
    "Lava Source Conversion":  ItemData(43032, ItemClassification.useful),   # lavaSourceConversion true
    "Phantom Spawning":        ItemData(43033, ItemClassification.useful),   # doInsomnia true
    "Warden Spawning":         ItemData(43034, ItemClassification.useful),   # doWardenSpawning true
}

# ── Filler items ───────────────────────────────────────────────────────────
# Physically given to the player on receipt.
# Items that are also in unlock_items above use the (Gift) suffix here.
# ──────────────────────────────────────────────────────────────────────────

filler_items: Dict[str, ItemData] = {

    # — Food Tier 1 ————————————————————————————————————————————————————————
    "Beetroot":            ItemData(43035, ItemClassification.filler),
    "Dried Kelp":          ItemData(43036, ItemClassification.filler),
    "Potato":              ItemData(43037, ItemClassification.filler),
    "Pufferfish":          ItemData(43038, ItemClassification.filler),
    "Tropical Fish":       ItemData(43039, ItemClassification.filler),
    "Cookie":              ItemData(43040, ItemClassification.filler),
    "Glow Berries":        ItemData(43041, ItemClassification.filler),
    "Melon Slice":         ItemData(43042, ItemClassification.filler),
    "Poisonous Potato":    ItemData(43043, ItemClassification.filler),
    "Spider Eye":          ItemData(43044, ItemClassification.filler),
    "Rotten Flesh":        ItemData(43045, ItemClassification.filler),

    # — Food Tier 2 ————————————————————————————————————————————————————————
    "Raw Chicken":         ItemData(43046, ItemClassification.filler),
    "Raw Mutton":          ItemData(43047, ItemClassification.filler),
    "Raw Beef":            ItemData(43048, ItemClassification.filler),
    "Raw Porkchop":        ItemData(43049, ItemClassification.filler),
    "Raw Rabbit":          ItemData(43050, ItemClassification.filler),
    "Bread":               ItemData(43051, ItemClassification.filler),
    "Rabbit Stew":         ItemData(43052, ItemClassification.filler),
    "Apple":               ItemData(43053, ItemClassification.filler),

    # — Food Tier 3 ————————————————————————————————————————————————————————
    "Cooked Porkchop":     ItemData(43054, ItemClassification.filler),
    "Steak":               ItemData(43055, ItemClassification.filler),
    "Pumpkin Pie":         ItemData(43056, ItemClassification.filler),
    "Golden Carrot":       ItemData(43057, ItemClassification.filler),

    # — Weapons to give ————————————————————————————————————————————————————
    "Wooden Sword":        ItemData(43058, ItemClassification.filler),
    "Stone Sword":         ItemData(43059, ItemClassification.filler),
    "Iron Sword":          ItemData(43060, ItemClassification.filler),
    "Diamond Sword":       ItemData(43061, ItemClassification.filler),
    "Wooden Axe":          ItemData(43062, ItemClassification.filler),
    "Stone Axe":           ItemData(43063, ItemClassification.filler),
    "Iron Axe":            ItemData(43064, ItemClassification.filler),
    "Diamond Axe":         ItemData(43065, ItemClassification.filler),
    "Leather Armor":       ItemData(43066, ItemClassification.filler),
    "Iron Armor":          ItemData(43067, ItemClassification.filler),
    "Diamond Armor":       ItemData(43068, ItemClassification.filler),
    "Trident (Gift)":      ItemData(43069, ItemClassification.filler),
    "Mace (Gift)":         ItemData(43070, ItemClassification.filler),
    "Bow (Gift)":          ItemData(43071, ItemClassification.filler),
    "Crossbow (Gift)":     ItemData(43072, ItemClassification.filler),
    "Arrow":               ItemData(43073, ItemClassification.filler),
    "Shield (Gift)":       ItemData(43074, ItemClassification.filler),

    # — Tools to give ——————————————————————————————————————————————————————
    "Wooden Pickaxe":      ItemData(43075, ItemClassification.filler),
    "Stone Pickaxe":       ItemData(43076, ItemClassification.filler),
    "Iron Pickaxe":        ItemData(43077, ItemClassification.filler),
    "Diamond Pickaxe":     ItemData(43078, ItemClassification.filler),
    "Wooden Shovel":       ItemData(43079, ItemClassification.filler),
    "Stone Shovel":        ItemData(43080, ItemClassification.filler),
    "Iron Shovel":         ItemData(43081, ItemClassification.filler),
    "Diamond Shovel":      ItemData(43082, ItemClassification.filler),

    # — Blocks ————————————————————————————————————————————————————————————
    "Cobblestone":         ItemData(43083, ItemClassification.filler),
    "Oak Planks":          ItemData(43084, ItemClassification.filler),
    "Dirt":                ItemData(43085, ItemClassification.filler),
    "Torch":               ItemData(43086, ItemClassification.filler),
    "Scaffolding":         ItemData(43087, ItemClassification.filler),

    # — Materials ——————————————————————————————————————————————————————————
    "Coal":                ItemData(43088, ItemClassification.filler),
    "Iron Ingot":          ItemData(43089, ItemClassification.filler),
    "Copper Ingot":        ItemData(43090, ItemClassification.filler),
    "Gold Ingot":          ItemData(43091, ItemClassification.filler),
    "Emerald":             ItemData(43092, ItemClassification.filler),
    "Lapis Lazuli":        ItemData(43093, ItemClassification.filler),
    "Redstone":            ItemData(43094, ItemClassification.filler),
    "Glowstone Dust":      ItemData(43095, ItemClassification.filler),
    "Amethyst Shard":      ItemData(43096, ItemClassification.filler),
    "Diamond":             ItemData(43097, ItemClassification.filler),
    "Netherite Scrap":     ItemData(43098, ItemClassification.filler),
    "Nether Quartz":       ItemData(43099, ItemClassification.filler),
    "Leather":             ItemData(43100, ItemClassification.filler),

    # — Utility ————————————————————————————————————————————————————————————
    "Bucket (Gift)":          ItemData(43101, ItemClassification.filler),
    "Compass":                ItemData(43102, ItemClassification.filler),
    "Fishing Rod (Gift)":     ItemData(43103, ItemClassification.filler),
    "Flint and Steel (Gift)": ItemData(43104, ItemClassification.filler),
    "Boat (Gift)":            ItemData(43105, ItemClassification.filler),
    "Spyglass (Gift)":        ItemData(43106, ItemClassification.filler),

    # — Junk ———————————————————————————————————————————————————————————————
    "Flower":              ItemData(43107, ItemClassification.filler),
    "Coral":               ItemData(43108, ItemClassification.filler),
    "Painting":            ItemData(43109, ItemClassification.filler),
    "Ink Sac":             ItemData(43110, ItemClassification.filler),
    "Dye":                 ItemData(43111, ItemClassification.filler),
    "Curse Enchanted Book": ItemData(43112, ItemClassification.filler),
}

# ── Combined table ─────────────────────────────────────────────────────────

item_table: Dict[str, ItemData] = {
    **progressive_items,
    **unlock_items,
    **gamerule_items,
    **filler_items,
}
