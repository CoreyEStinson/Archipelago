from typing import Dict, NamedTuple


class LocationData(NamedTuple):
    code: int    # AP location ID — must match advancements.json in the mod
    region: str  # which region gates access to this location


ADVANCEMENT_LOCATION_BASE_ID = 20000
BOSS_KILL_LOCATION_BASE_ID = 21000
LOOTABLE_CHECK_BASE_ID = 22000

# Region summary:
#   "Overworld" — accessible from the start (story, adventure, husbandry)
#   "Nether"    — requires entering the Nether
#   "The End"   — requires entering The End

location_table: Dict[str, LocationData] = {

    # ── Story (Minecraft tab) ─────────────────────────────────── Overworld ─

    "Stone Age":                    LocationData(20000, "Overworld"),
    "Getting an Upgrade":           LocationData(20001, "Overworld"),
    "Acquire Hardware":             LocationData(20002, "Overworld"),
    "Suit Up":                      LocationData(20003, "Overworld"),
    "Hot Stuff":                    LocationData(20004, "Overworld"),
    "Isn't It Iron Pick":           LocationData(20005, "Overworld"),
    "Not Today, Thank You":         LocationData(20006, "Overworld"),
    "Ice Bucket Challenge":         LocationData(20007, "Overworld"),
    "Diamonds!":                    LocationData(20008, "Overworld"),
    "We Need to Go Deeper":         LocationData(20009, "Overworld"),
    "Cover Me with Diamonds":       LocationData(20010, "Overworld"),
    "Zombie Doctor":                LocationData(20011, "Overworld"),
    "Eye Spy":                      LocationData(20012, "Overworld"),
    "The End?":                     LocationData(20013, "Overworld"),
    "Enchant Item":                 LocationData(20014, "Overworld"),

    # ── Nether tab ───────────────────────────────────────────────── Nether ─

    "Return to Sender":             LocationData(20015, "Nether"),
    "Those Were the Days":          LocationData(20016, "Nether"),
    "Hidden in the Depths":         LocationData(20017, "Nether"),
    "Subspace Bubble":              LocationData(20018, "Nether"),
    "A Terrible Fortress":          LocationData(20019, "Nether"),
    "Who Is Cutting Onions?":       LocationData(20020, "Nether"),
    "Oh Shiny!":                    LocationData(20021, "Nether"),
    "This Boat Has Legs":           LocationData(20022, "Nether"),
    "Uneasy Alliance":              LocationData(20023, "Nether"),
    "War Pigs":                     LocationData(20024, "Nether"),
    "Cover Me in Debris":           LocationData(20025, "Nether"),
    "Spooky Scary Skeleton":        LocationData(20026, "Nether"),
    "Into Fire":                    LocationData(20027, "Nether"),
    "Not Quite 'Nine' Lives":       LocationData(20028, "Nether"),
    "Feels Like Home":              LocationData(20029, "Nether"),
    "Hot Tourist Destinations":     LocationData(20030, "Nether"),
    "Withering Heights":            LocationData(20031, "Nether"),
    "Local Brewery":                LocationData(20032, "Nether"),
    "Bring Home the Beacon":        LocationData(20033, "Nether"),
    "A Furious Cocktail":           LocationData(20034, "Nether"),
    "Beaconator":                   LocationData(20035, "Nether"),
    "How Did We Get Here?":         LocationData(20036, "Nether"),

    # ── The End tab ──────────────────────────────────────────── The End ─

    "Free the End":                     LocationData(20037, "The End"),
    "The Next Generation":              LocationData(20038, "The End"),
    "Remote Getaway":                   LocationData(20039, "The End"),
    "The End... Again...":              LocationData(20040, "The End"),
    "You Need a Mint":                  LocationData(20041, "The End"),
    "The City at the End of the Game":  LocationData(20042, "The End"),
    "Sky's the Limit":                  LocationData(20043, "The End"),
    "Great View From Up Here":          LocationData(20044, "The End"),

    # ── Adventure tab ─────────────────────────────────────────── Overworld ─
    
    "Voluntary Exile":              LocationData(20045, "Overworld"),
    "Country Lode, Take Me Home":   LocationData(20046, "Overworld"),
    "Is It a Bird?":                LocationData(20047, "Overworld"),
    "Monster Hunter":               LocationData(20048, "Overworld"),
    "The Power of Books":           LocationData(20049, "Overworld"),
    "What a Deal!":                 LocationData(20050, "Overworld"),
    "Crafting a New Look":          LocationData(20051, "Overworld"),
    "Sticky Situation":             LocationData(20052, "Overworld"),
    "Ol' Betsy":                    LocationData(20053, "Overworld"),
    "Surge Protector":              LocationData(20054, "Overworld"),
    "Caves & Cliffs":               LocationData(20055, "Overworld"),
    "Respecting the Remnants":      LocationData(20056, "Overworld"),
    "Sneak 100":                    LocationData(20057, "Overworld"),
    "Sweet Dreams":                 LocationData(20058, "Overworld"),
    "Hero of the Village":          LocationData(20059, "Overworld"),
    "Is It a Plane?":               LocationData(20060, "Overworld"),
    "A Throwaway Joke":             LocationData(20061, "Overworld"),
    "It Spreads":                   LocationData(20062, "Overworld"),
    "Take Aim":                     LocationData(20063, "Overworld"),
    "Monsters Hunted":              LocationData(20064, "Overworld"),
    "Postmortal":                   LocationData(20065, "Overworld"),
    "Hired Help":                   LocationData(20066, "Overworld"),
    "Star Trader":                  LocationData(20067, "Overworld"),
    "Smithing with Style":          LocationData(20068, "Overworld"),
    "Two Birds, One Arrow":         LocationData(20069, "Overworld"),
    "Who's the Pillager Now?":      LocationData(20070, "Overworld"),
    "Arbalistic":                   LocationData(20071, "Overworld"),
    "Careful Restoration":          LocationData(20072, "Overworld"),
    "Adventuring Time":             LocationData(20073, "Overworld"),
    "Sound of Music":               LocationData(20074, "Overworld"),
    "Light as a Rabbit":            LocationData(20075, "Overworld"),
    "Is It a Balloon?":             LocationData(20076, "Overworld"),
    "Very Very Frightening":        LocationData(20077, "Overworld"),
    "Sniper Duel":                  LocationData(20078, "Overworld"),
    "Bullseye":                     LocationData(20079, "Overworld"),
    "Isn't It Scute?":              LocationData(20080, "Overworld"),
    "Minecraft: Trial(s) Edition":  LocationData(20081, "Overworld"),
    "Lighten Up":                   LocationData(20082, "Overworld"),
    "Who Needs Rockets?":           LocationData(20083, "Overworld"),
    "Under Lock and Key":           LocationData(20084, "Overworld"),
    "Revaulting":                   LocationData(20085, "Overworld"),
    "Blowback":                     LocationData(20086, "Overworld"),
    "Over-Overkill":                LocationData(20087, "Overworld"),
    "Crafters Crafting Crafters":   LocationData(20088, "Overworld"),

    # ── Husbandry tab ─────────────────────────────────────────── Overworld ─

    "Bee Our Guest":                LocationData(20089, "Overworld"),
    "Repopulation":                 LocationData(20090, "Overworld"),
    "You've Got a Friend in Me":    LocationData(20091, "Overworld"),
    "Whatever Floats Your Goat!":   LocationData(20092, "Overworld"),
    "Best Friends Forever":         LocationData(20093, "Overworld"),
    "Glow and Behold!":             LocationData(20094, "Overworld"),
    "Fishy Business":               LocationData(20095, "Overworld"),
    "Total Beelocation":            LocationData(20096, "Overworld"),
    "Bukkit Bukkit":                LocationData(20097, "Overworld"),
    "Little Sniffs":                LocationData(20098, "Overworld"),
    "A Seedy Place":                LocationData(20099, "Overworld"),
    "Wax On":                       LocationData(20100, "Overworld"),
    "Two by Two":                   LocationData(20101, "Overworld"),
    "Allay Delivers Cake":          LocationData(20102, "Overworld"),
    "A Complete Catalogue":         LocationData(20103, "Overworld"),
    "Tactical Fishing":             LocationData(20104, "Overworld"),
    "When the Squad Hops into Town": LocationData(20105, "Overworld"),
    "Smells Interesting":           LocationData(20106, "Overworld"),
    "A Balanced Diet":              LocationData(20107, "Overworld"),
    "Serious Dedication":           LocationData(20108, "Overworld"),
    "Wax Off":                      LocationData(20109, "Overworld"),
    "The Cutest Predator":          LocationData(20110, "Overworld"),
    "With Our Powers Combined!":    LocationData(20111, "Overworld"),
    "Planting the Past":            LocationData(20112, "Overworld"),
    "Kill Axolotl Target":          LocationData(20113, "Overworld"),
    "Repair Wolf Armor":            LocationData(20114, "Overworld"),
    "Whole Pack":                   LocationData(20115, "Overworld"),
    "Remove Wolf Armor":            LocationData(20116, "Overworld"),

    # ── Boss Kills ────────────────────────────────────────────────────────────
    "Ender Dragon Kill":            LocationData(21000, "The End"),
    "Wither Kill":                  LocationData(21001, "Nether"),
    "Elder Guardian Kill":          LocationData(21002, "Overworld"),
    "Warden Kill":                  LocationData(21003, "Overworld"),

    # ── Lootable Checks ───────────────────────────────────────────────────────
    # All 50 possible checks are defined here.
    # Only the first N are included in any given game, controlled by the
    # lootable_checks YAML option (default 20).
    # IDs start at 22000

    "Lootable Check 1":  LocationData(22000, "Overworld"),
    "Lootable Check 2":  LocationData(22001, "Overworld"),
    "Lootable Check 3":  LocationData(22002, "Overworld"),
    "Lootable Check 4":  LocationData(22003, "Overworld"),
    "Lootable Check 5":  LocationData(22004, "Overworld"),
    "Lootable Check 6":  LocationData(22005, "Overworld"),
    "Lootable Check 7":  LocationData(22006, "Overworld"),
    "Lootable Check 8":  LocationData(22007, "Overworld"),
    "Lootable Check 9":  LocationData(22008, "Overworld"),
    "Lootable Check 10": LocationData(22009, "Overworld"),
    "Lootable Check 11": LocationData(22010, "Overworld"),
    "Lootable Check 12": LocationData(22011, "Overworld"),
    "Lootable Check 13": LocationData(22012, "Overworld"),
    "Lootable Check 14": LocationData(22013, "Overworld"),
    "Lootable Check 15": LocationData(22014, "Overworld"),
    "Lootable Check 16": LocationData(22015, "Overworld"),
    "Lootable Check 17": LocationData(22016, "Overworld"),
    "Lootable Check 18": LocationData(22017, "Overworld"),
    "Lootable Check 19": LocationData(22018, "Overworld"),
    "Lootable Check 20": LocationData(22019, "Overworld"),
    "Lootable Check 21": LocationData(22020, "Overworld"),
    "Lootable Check 22": LocationData(22021, "Overworld"),
    "Lootable Check 23": LocationData(22022, "Overworld"),
    "Lootable Check 24": LocationData(22023, "Overworld"),
    "Lootable Check 25": LocationData(22024, "Overworld"),
    "Lootable Check 26": LocationData(22025, "Overworld"),
    "Lootable Check 27": LocationData(22026, "Overworld"),
    "Lootable Check 28": LocationData(22027, "Overworld"),
    "Lootable Check 29": LocationData(22028, "Overworld"),
    "Lootable Check 30": LocationData(22029, "Overworld"),
    "Lootable Check 31": LocationData(22030, "Overworld"),
    "Lootable Check 32": LocationData(22031, "Overworld"),
    "Lootable Check 33": LocationData(22032, "Overworld"),
    "Lootable Check 34": LocationData(22033, "Overworld"),
    "Lootable Check 35": LocationData(22034, "Overworld"),
    "Lootable Check 36": LocationData(22035, "Overworld"),
    "Lootable Check 37": LocationData(22036, "Overworld"),
    "Lootable Check 38": LocationData(22037, "Overworld"),
    "Lootable Check 39": LocationData(22038, "Overworld"),
    "Lootable Check 40": LocationData(22039, "Overworld"),
    "Lootable Check 41": LocationData(22040, "Overworld"),
    "Lootable Check 42": LocationData(22041, "Overworld"),
    "Lootable Check 43": LocationData(22042, "Overworld"),
    "Lootable Check 44": LocationData(22043, "Overworld"),
    "Lootable Check 45": LocationData(22044, "Overworld"),
    "Lootable Check 46": LocationData(22045, "Overworld"),
    "Lootable Check 47": LocationData(22046, "Overworld"),
    "Lootable Check 48": LocationData(22047, "Overworld"),
    "Lootable Check 49": LocationData(22048, "Overworld"),
    "Lootable Check 50": LocationData(22049, "Overworld"),
}
