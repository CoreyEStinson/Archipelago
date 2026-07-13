import math
from typing import Dict, Any, List

from worlds.AutoWorld import World
from BaseClasses import Region, Location, Item

from .items import (
    item_table,
    unlock_items,
    gamerule_items,
    filler_items,
    PROGRESSIVE_ITEM_COUNTS,
)
from .locations import location_table
from .options import MinecraftArchipelagoOptions
from .rules import set_rules as apply_rules

LOOTABLE_CHECK_BASE_ID       = 42500
TOTAL_LOOTABLE_CHECKS_DEFINED = 42   # how many are in locations.py


class MinecraftArchipelagoItem(Item):
    game = "Minecraft Archipelago"


class MinecraftArchipelagoLocation(Location):
    game = "Minecraft Archipelago"


class MinecraftArchipelagoWorld(World):
    """A Minecraft randomizer for Fabric 1.21.1.
    Advancements are locations. Items unlock gear tiers, mechanics, and world rules."""

    game = "Minecraft Archipelago"
    options_dataclass = MinecraftArchipelagoOptions
    options: MinecraftArchipelagoOptions

    # These two dicts are required by Archipelago.
    # They tell the server what item and location IDs this game uses.
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}


    def generate_early(self) -> None:
        # Clamp required_lootable_checks so it never exceeds the pool size
        if self.options.required_lootable_checks.value \
                > self.options.lootable_checks.value:
            self.options.required_lootable_checks.value = \
                self.options.lootable_checks.value

        # If lootable checks pool is empty, lootable win condition can't be active
        if self.options.lootable_checks.value == 0:
            self.options.required_lootable_checks.value = 0

        # Validate: at least one win condition must be active
        advancement_active  = self.options.advancement_goal.value > 0
        bosses_active       = len(self.options.required_boss_kills.value) > 0
        lootable_active     = self.options.required_lootable_checks.value > 0
        collections_active  = len(self.options.required_item_collections.value) > 0  # NEW

        if not (advancement_active or bosses_active or lootable_active or collections_active):
            raise Exception(
                f"Minecraft Archipelago ({self.player_name}): No win conditions are "
                f"active. Enable at least one: set advancement_goal > 0, add bosses to "
                f"required_boss_kills, set required_lootable_checks > 0, or add "
                f"collections to required_item_collections."
            )


    # ── Region and location setup ─────────────────────────────────────────

    def create_regions(self) -> None:
        menu      = Region("Menu",      self.player, self.multiworld)
        overworld = Region("Overworld", self.player, self.multiworld)
        nether    = Region("Nether",    self.player, self.multiworld)
        the_end   = Region("The End",   self.player, self.multiworld)

        region_map = {
            "Overworld": overworld,
            "Nether":    nether,
            "The End":   the_end,
        }

        lootable_limit = self.options.lootable_checks.value

        # Add every location from locations.py to its region
        for loc_name, loc_data in location_table.items():

            # Skip lootable checks that exceed the configured limit for this game
            if loc_data.code >= LOOTABLE_CHECK_BASE_ID:
                index = loc_data.code - LOOTABLE_CHECK_BASE_ID  # 0-based
                if index >= lootable_limit:
                    continue

            target_region = region_map[loc_data.region]
            location = MinecraftArchipelagoLocation(
                self.player, loc_name, loc_data.code, target_region
            )
            target_region.locations.append(location)

        # Connect regions with named entrances.
        # These names must match exactly what rules.py passes to get_entrance().
        menu.connect(overworld, "Menu -> Overworld")
        overworld.connect(nether, "Overworld -> Nether")
        nether.connect(the_end, "Nether -> The End")

        self.multiworld.regions += [menu, overworld, nether, the_end]

    # ── Item pool ─────────────────────────────────────────────────────────

    def create_items(self) -> None:
        pool: List[str] = []

        # Progressive items — one copy per tier
        # (e.g. Progressive Tools appears 4 times: stone, iron, diamond, netherite)
        for name, count in PROGRESSIVE_ITEM_COUNTS.items():
            pool.extend([name] * count)

        # Unlock items — one copy each
        for name in unlock_items:
            pool.append(name)

        # Gamerule items — one copy each
        for name in gamerule_items:
            pool.append(name)

        # Active locations = everything in location_table except the lootable checks
        # that were skipped by create_regions(), plus however many ARE active.
        lootable_limit    = self.options.lootable_checks.value
        total_active      = (
            len(location_table)
            - TOTAL_LOOTABLE_CHECKS_DEFINED
            + lootable_limit
        )

        # Fill any remaining slots with random filler items.
        # There are 112 locations and 39 important items, so we need 73 fillers.
        filler_pool = list(filler_items.keys())
        remaining = total_active - len(pool)

        if remaining < 0:
            raise Exception(
                f"Too many items ({len(pool)}) for available locations ({len(location_table)})"
            )

        for _ in range(remaining):
            pool.append(self.random.choice(filler_pool))

        # Create Item objects and add them all to the multiworld pool
        for name in pool:
            self.multiworld.itempool.append(self.create_item(name))

    def create_item(self, name: str) -> MinecraftArchipelagoItem:
        data = item_table[name]
        return MinecraftArchipelagoItem(
            name, data.classification, data.code, self.player
        )

    def get_filler_item_name(self) -> str:
        # Called by the base class if it ever needs an extra filler on its own
        return self.random.choice(list(filler_items.keys()))

    # ── Rules ─────────────────────────────────────────────────────────────

    def set_rules(self) -> None:

        # Map used for building location-based boss kill conditions
        _BOSS_LOCATION_NAMES = {
            "ender_dragon": "Ender Dragon Kill",
            "wither":        "Wither Kill",
            "elder_guardian":"Elder Guardian Kill",
            "warden":        "Warden Kill",
        }

        from .rules import set_rules as apply_rules
        apply_rules(self)

        conditions = []

        # ── Advancement goal ──────────────────────────────────────────────────
        if self.options.advancement_goal.value > 0:
            # Reaching The End is a strong proxy for overall progression.
            # The actual % check is done at runtime by the mod.
            conditions.append(
                lambda state: state.can_reach("The End", "Region", self.player)
            )

        # ── Boss kills ────────────────────────────────────────────────────────
        # Each required boss maps to a specific location that must be reachable.
        # Existing rules.py rules handle region + item prerequisites correctly.
        for boss in self.options.required_boss_kills.value:
            loc_name = _BOSS_LOCATION_NAMES.get(boss)
            if loc_name:
                conditions.append(
                    lambda state, ln=loc_name:
                        state.can_reach(ln, "Location", self.player)
                )

        # ── Lootable checks ───────────────────────────────────────────────────
        # All lootable check locations are in the Overworld with no gates,
        # so they're always reachable — no extra condition needed here.

        # ── Fallback (should not be hit due to generate_early validation) ─────
        if not conditions:
            conditions.append(lambda state: True)

        self.multiworld.completion_condition[self.player] = \
            lambda state: all(c(state) for c in conditions)

    # ── Slot data ─────────────────────────────────────────────────────────

    def fill_slot_data(self) -> Dict[str, Any]:
        # This dict is sent to the mod on connect.
        # SlotData.java reads these values — key names must match exactly.
        return {
            "advancement_goal": self.options.advancement_goal.value,
            "death_link": self.options.death_link.value,
            "lootable_checks": self.options.lootable_checks.value,
            "required_boss_kills": sorted(list(self.options.required_boss_kills.value)),
            "required_lootable_checks": self.options.required_lootable_checks.value,
            "required_item_collections": sorted(list(self.options.required_item_collections.value)),
        }