from typing import Dict, NamedTuple


class LocationData(NamedTuple):
    code: int    # AP location ID — must match advancements.json in the mod
    region: str  # which region gates access to this location


LOCATION_BASE_ID = 42001

# Region summary:
#   "Overworld" — accessible from the start (story, adventure, husbandry)
#   "Nether"    — requires entering the Nether
#   "The End"   — requires entering The End

location_table: Dict[str, LocationData] = {

    # ── Story (Minecraft tab) ─────────────────────────────────── Overworld ─

    "Stone Age":                    LocationData(42001, "Overworld"),
    "Getting an Upgrade":           LocationData(42002, "Overworld"),
    "Acquire Hardware":             LocationData(42003, "Overworld"),
    "Suit Up":                      LocationData(42004, "Overworld"),
    "Hot Stuff":                    LocationData(42005, "Overworld"),
    "Isn't It Iron Pick":           LocationData(42006, "Overworld"),
    "Not Today, Thank You":         LocationData(42007, "Overworld"),
    "Ice Bucket Challenge":         LocationData(42008, "Overworld"),
    "Diamonds!":                    LocationData(42009, "Overworld"),
    "We Need to Go Deeper":         LocationData(42010, "Overworld"),
    "Cover Me with Diamonds":       LocationData(42011, "Overworld"),
    "Zombie Doctor":                LocationData(42012, "Overworld"),
    "Eye Spy":                      LocationData(42013, "Overworld"),
    "The End?":                     LocationData(42014, "Overworld"),

    # ── Nether tab ───────────────────────────────────────────────── Nether ─

    "Return to Sender":             LocationData(42015, "Nether"),
    "Those Were the Days":          LocationData(42016, "Nether"),
    "Hidden in the Depths":         LocationData(42017, "Nether"),
    "Subspace Bubble":              LocationData(42018, "Nether"),
    "A Terrible Fortress":          LocationData(42019, "Nether"),
    "Who Is Cutting Onions?":       LocationData(42020, "Nether"),
    "Oh Shiny!":                    LocationData(42021, "Nether"),
    "This Boat Has Legs":           LocationData(42022, "Nether"),
    "Uneasy Alliance":              LocationData(42023, "Nether"),
    "War Pigs":                     LocationData(42024, "Nether"),
    "Cover Me in Debris":           LocationData(42025, "Nether"),
    "Spooky Scary Skeleton":        LocationData(42026, "Nether"),
    "Into Fire":                    LocationData(42027, "Nether"),
    "Not Quite 'Nine' Lives":       LocationData(42028, "Nether"),
    "Feels Like Home":              LocationData(42029, "Nether"),
    "Hot Tourist Destinations":     LocationData(42030, "Nether"),
    "Withering Heights":            LocationData(42031, "Nether"),
    "Local Brewery":                LocationData(42032, "Nether"),
    "Bring Home the Beacon":        LocationData(42033, "Nether"),
    "A Furious Cocktail":           LocationData(42034, "Nether"),
    "Beaconator":                   LocationData(42035, "Nether"),
    "How Did We Get Here?":         LocationData(42036, "Nether"),

    # ── The End tab ──────────────────────────────────────────── The End ─

    "Free the End":                     LocationData(42037, "The End"),
    "The Next Generation":              LocationData(42038, "The End"),
    "Remote Getaway":                   LocationData(42039, "The End"),
    "The End... Again...":              LocationData(42040, "The End"),
    "You Need a Mint":                  LocationData(42041, "The End"),
    "The City at the End of the Game":  LocationData(42042, "The End"),
    "Sky's the Limit":                  LocationData(42043, "The End"),
    "Great View From Up Here":          LocationData(42044, "The End"),

    # ── Adventure tab ─────────────────────────────────────────── Overworld ─

    "Heart Transplanter":           LocationData(42045, "Overworld"),
    "Voluntary Exile":              LocationData(42046, "Overworld"),
    "Country Lode, Take Me Home":   LocationData(42047, "Overworld"),
    "Is It a Bird?":                LocationData(42048, "Overworld"),
    "Monster Hunter":               LocationData(42049, "Overworld"),
    "The Power of Books":           LocationData(42050, "Overworld"),
    "What a Deal!":                 LocationData(42051, "Overworld"),
    "Crafting a New Look":          LocationData(42052, "Overworld"),
    "Sticky Situation":             LocationData(42053, "Overworld"),
    "Ol' Betsy":                    LocationData(42054, "Overworld"),
    "Surge Protector":              LocationData(42055, "Overworld"),
    "Caves & Cliffs":               LocationData(42056, "Overworld"),
    "Respecting the Remnants":      LocationData(42057, "Overworld"),
    "Sneak 100":                    LocationData(42058, "Overworld"),
    "Sweet Dreams":                 LocationData(42059, "Overworld"),
    "Hero of the Village":          LocationData(42060, "Overworld"),
    "Is It a Plane?":               LocationData(42061, "Overworld"),
    "A Throwaway Joke":             LocationData(42062, "Overworld"),
    "It Spreads":                   LocationData(42063, "Overworld"),
    "Take Aim":                     LocationData(42064, "Overworld"),
    "Monsters Hunted":              LocationData(42065, "Overworld"),
    "Postmortal":                   LocationData(42066, "Overworld"),
    "Hired Help":                   LocationData(42067, "Overworld"),
    "Star Trader":                  LocationData(42068, "Overworld"),
    "Smithing with Style":          LocationData(42069, "Overworld"),
    "Two Birds, One Arrow":         LocationData(42070, "Overworld"),
    "Who's the Pillager Now?":      LocationData(42071, "Overworld"),
    "Arbalistic":                   LocationData(42072, "Overworld"),
    "Careful Restoration":          LocationData(42073, "Overworld"),
    "Adventuring Time":             LocationData(42074, "Overworld"),
    "Sound of Music":               LocationData(42075, "Overworld"),
    "Light as a Rabbit":            LocationData(42076, "Overworld"),
    "Is It a Balloon?":             LocationData(42077, "Overworld"),
    "Very Very Frightening":        LocationData(42078, "Overworld"),
    "Sniper Duel":                  LocationData(42079, "Overworld"),
    "Bullseye":                     LocationData(42080, "Overworld"),
    "Isn't It Scute?":              LocationData(42081, "Overworld"),
    "Minecraft: Trial(s) Edition":  LocationData(42082, "Overworld"),
    "Lighten Up":                   LocationData(42083, "Overworld"),
    "Who Needs Rockets?":           LocationData(42084, "Overworld"),
    "Under Lock and Key":           LocationData(42085, "Overworld"),
    "Revaulting":                   LocationData(42086, "Overworld"),
    "Blowback":                     LocationData(42087, "Overworld"),
    "Over-Overkill":                LocationData(42088, "Overworld"),

    # ── Husbandry tab ─────────────────────────────────────────── Overworld ─

    "Bee Our Guest":                LocationData(42089, "Overworld"),
    "Repopulation":                 LocationData(42090, "Overworld"),
    "You've Got a Friend in Me":    LocationData(42091, "Overworld"),
    "Whatever Floats Your Goat!":   LocationData(42092, "Overworld"),
    "Best Friends Forever":         LocationData(42093, "Overworld"),
    "Glow and Behold!":             LocationData(42094, "Overworld"),
    "Fishy Business":               LocationData(42095, "Overworld"),
    "Total Beelocation":            LocationData(42096, "Overworld"),
    "Bukkit Bukkit":                LocationData(42097, "Overworld"),
    "Little Sniffs":                LocationData(42098, "Overworld"),
    "A Seedy Place":                LocationData(42099, "Overworld"),
    "Wax On":                       LocationData(42100, "Overworld"),
    "Two by Two":                   LocationData(42101, "Overworld"),
    "Allay Delivers Cake":          LocationData(42102, "Overworld"),
    "A Complete Catalogue":         LocationData(42103, "Overworld"),
    "Tactical Fishing":             LocationData(42104, "Overworld"),
    "When the Squad Hops into Town": LocationData(42105, "Overworld"),
    "Smells Interesting":           LocationData(42106, "Overworld"),
    "A Balanced Diet":              LocationData(42107, "Overworld"),
    "Serious Dedication":           LocationData(42108, "Overworld"),
    "Wax Off":                      LocationData(42109, "Overworld"),
    "The Cutest Predator":          LocationData(42110, "Overworld"),
    "With Our Powers Combined!":    LocationData(42111, "Overworld"),
    "Planting the Past":            LocationData(42112, "Overworld"),
}

LOOT_CHECK_BASE_ID = 42212
LOOT_CHECK_MAX = 50