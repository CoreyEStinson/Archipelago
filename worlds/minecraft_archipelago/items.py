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
    "Flint and Steel":  ItemData(43016, ItemClassification.progression),
    "Trident":          ItemData(43017, ItemClassification.useful),
    "Bow":              ItemData(43018, ItemClassification.useful),
    "Fishing Rod":      ItemData(43019, ItemClassification.useful),
    "Boat":             ItemData(43020, ItemClassification.useful),
    "Crossbow":         ItemData(43021, ItemClassification.useful),
    "Ender Pearl":      ItemData(43022, ItemClassification.progression),
    "Eye of Ender":     ItemData(43023, ItemClassification.progression),

    # ── Block/structure unlock items ──────────────────────────────────────────
    "Beacon":          ItemData(43024, ItemClassification.progression),
    "Conduit":         ItemData(43025, ItemClassification.progression),
    "Bed":             ItemData(43026, ItemClassification.progression),
    "Furnace":         ItemData(43027, ItemClassification.progression),
    "Anvil":           ItemData(43028, ItemClassification.progression),
    "Brewing Stand":   ItemData(43029, ItemClassification.progression),
    "Ender Chest":     ItemData(43030, ItemClassification.useful),
    "Shulker Box":     ItemData(43031, ItemClassification.useful),
    "Lightning Rod":   ItemData(43032, ItemClassification.progression),
    "Composter":       ItemData(43033, ItemClassification.useful),
    "Smithing Table":  ItemData(43034, ItemClassification.progression),
    "Grindstone":      ItemData(43035, ItemClassification.useful),
    "Torch":           ItemData(43036, ItemClassification.progression),
    "Campfire":        ItemData(43037, ItemClassification.useful),
    "Target":          ItemData(43038, ItemClassification.progression),
    "TNT":             ItemData(43039, ItemClassification.useful),
}



# ── Gamerule items ─────────────────────────────────────────────────────────
# Each permanently changes a world rule when received.
# Comments show the 1.21.1 camelCase gamerule name and the value set on receipt.
# ──────────────────────────────────────────────────────────────────────────

gamerule_items: Dict[str, ItemData] = {
    "Raids":                   ItemData(43040, ItemClassification.progression),
    "Disable Mob Griefing":    ItemData(43041, ItemClassification.useful),
    "No Fall Damage":          ItemData(43042, ItemClassification.useful),
    "No Fire Damage":          ItemData(43043, ItemClassification.useful),
    "No Freeze Damage":        ItemData(43044, ItemClassification.useful),
    "Keep Inventory":          ItemData(43045, ItemClassification.useful),
    "Wandering Traders":       ItemData(43046, ItemClassification.useful),
    "Water Source Conversion": ItemData(43047, ItemClassification.useful),
    "Lava Source Conversion":  ItemData(43048, ItemClassification.useful),
    "Phantom Spawning":        ItemData(43049, ItemClassification.progression),
    "Warden Spawning":         ItemData(43050, ItemClassification.progression),
}

# ── Filler items ───────────────────────────────────────────────────────────
# Physically given to the player on receipt.
# Items that are also in unlock_items above use the (Gift) suffix here.
# ──────────────────────────────────────────────────────────────────────────

filler_items: Dict[str, ItemData] = {

    # — Food Tier 1 ————————————————————————————————————————————————————————
    "Beetroot":            ItemData(43051, ItemClassification.filler),
    "Dried Kelp":          ItemData(43052, ItemClassification.filler),
    "Potato":              ItemData(43053, ItemClassification.filler),
    "Pufferfish":          ItemData(43054, ItemClassification.filler),
    "Tropical Fish":       ItemData(43055, ItemClassification.filler),
    "Cookie":              ItemData(43056, ItemClassification.filler),
    "Glow Berries":        ItemData(43057, ItemClassification.filler),
    "Melon Slice":         ItemData(43058, ItemClassification.filler),
    "Poisonous Potato":    ItemData(43059, ItemClassification.filler),
    "Spider Eye":          ItemData(43060, ItemClassification.filler),
    "Rotten Flesh":        ItemData(43061, ItemClassification.filler),

    # — Food Tier 2 ————————————————————————————————————————————————————————
    "Raw Chicken":         ItemData(43062, ItemClassification.filler),
    "Raw Mutton":          ItemData(43063, ItemClassification.filler),
    "Raw Beef":            ItemData(43064, ItemClassification.filler),
    "Raw Porkchop":        ItemData(43065, ItemClassification.filler),
    "Raw Rabbit":          ItemData(43066, ItemClassification.filler),
    "Bread":               ItemData(43067, ItemClassification.filler),
    "Rabbit Stew":         ItemData(43068, ItemClassification.filler),
    "Apple":               ItemData(43069, ItemClassification.filler),

    # — Food Tier 3 ————————————————————————————————————————————————————————
    "Cooked Porkchop":     ItemData(43070, ItemClassification.filler),
    "Steak":               ItemData(43071, ItemClassification.filler),
    "Pumpkin Pie":         ItemData(43072, ItemClassification.filler),
    "Golden Carrot":       ItemData(43073, ItemClassification.filler),

    # — Weapons to give ————————————————————————————————————————————————————
    "Wooden Sword":        ItemData(43074, ItemClassification.filler),
    "Stone Sword":         ItemData(43075, ItemClassification.filler),
    "Iron Sword":          ItemData(43076, ItemClassification.filler),
    "Diamond Sword":       ItemData(43077, ItemClassification.filler),
    "Wooden Axe":          ItemData(43078, ItemClassification.filler),
    "Stone Axe":           ItemData(43079, ItemClassification.filler),
    "Iron Axe":            ItemData(43080, ItemClassification.filler),
    "Diamond Axe":         ItemData(43081, ItemClassification.filler),
    "Leather Armor":       ItemData(43082, ItemClassification.filler),
    "Iron Armor":          ItemData(43083, ItemClassification.filler),
    "Diamond Armor":       ItemData(43084, ItemClassification.filler),
    "Trident (Gift)":      ItemData(43085, ItemClassification.filler),
    "Mace (Gift)":         ItemData(43086, ItemClassification.filler),
    "Bow (Gift)":          ItemData(43087, ItemClassification.filler),
    "Crossbow (Gift)":     ItemData(43088, ItemClassification.filler),
    "Arrow":               ItemData(43089, ItemClassification.filler),
    "Shield (Gift)":       ItemData(43090, ItemClassification.filler),

    # — Tools to give ——————————————————————————————————————————————————————
    "Wooden Pickaxe":      ItemData(43091, ItemClassification.filler),
    "Stone Pickaxe":       ItemData(43092, ItemClassification.filler),
    "Iron Pickaxe":        ItemData(43093, ItemClassification.filler),
    "Diamond Pickaxe":     ItemData(43094, ItemClassification.filler),
    "Wooden Shovel":       ItemData(43095, ItemClassification.filler),
    "Stone Shovel":        ItemData(43096, ItemClassification.filler),
    "Iron Shovel":         ItemData(43097, ItemClassification.filler),
    "Diamond Shovel":      ItemData(43098, ItemClassification.filler),

    # — Blocks ————————————————————————————————————————————————————————————
    "Cobblestone":         ItemData(43099, ItemClassification.filler),
    "Oak Planks":          ItemData(43100, ItemClassification.filler),
    "Dirt":                ItemData(43101, ItemClassification.filler),
    "Torch":               ItemData(43102, ItemClassification.filler),
    "Scaffolding":         ItemData(43103, ItemClassification.filler),

    # — Materials ——————————————————————————————————————————————————————————
    "Coal":                ItemData(43104, ItemClassification.filler),
    "Iron Ingot":          ItemData(43105, ItemClassification.filler),
    "Copper Ingot":        ItemData(43106, ItemClassification.filler),
    "Gold Ingot":          ItemData(43107, ItemClassification.filler),
    "Emerald":             ItemData(43108, ItemClassification.filler),
    "Lapis Lazuli":        ItemData(43109, ItemClassification.filler),
    "Redstone":            ItemData(43110, ItemClassification.filler),
    "Glowstone Dust":      ItemData(43111, ItemClassification.filler),
    "Amethyst Shard":      ItemData(43112, ItemClassification.filler),
    "Diamond":             ItemData(43113, ItemClassification.filler),
    "Netherite Scrap":     ItemData(43114, ItemClassification.filler),
    "Nether Quartz":       ItemData(43115, ItemClassification.filler),
    "Leather":             ItemData(43116, ItemClassification.filler),

    # — Utility ————————————————————————————————————————————————————————————
    "Bucket (Gift)":          ItemData(43117, ItemClassification.filler),
    "Compass":                ItemData(43118, ItemClassification.filler),
    "Fishing Rod (Gift)":     ItemData(43119, ItemClassification.filler),
    "Flint and Steel (Gift)": ItemData(43120, ItemClassification.filler),
    "Boat (Gift)":            ItemData(43121, ItemClassification.filler),
    "Spyglass (Gift)":        ItemData(43122, ItemClassification.filler),

    # — Junk ———————————————————————————————————————————————————————————————
    "Flower":              ItemData(43123, ItemClassification.filler),
    "Coral":               ItemData(43124, ItemClassification.filler),
    "Painting":            ItemData(43125, ItemClassification.filler),
    "Ink Sac":             ItemData(43126, ItemClassification.filler),
    "Dye":                 ItemData(43127, ItemClassification.filler),
    "Curse Enchanted Book": ItemData(43128, ItemClassification.filler),
}

# ── Combined table ─────────────────────────────────────────────────────────

item_table: Dict[str, ItemData] = {
    **progressive_items,
    **unlock_items,
    **gamerule_items,
    **filler_items,
}
