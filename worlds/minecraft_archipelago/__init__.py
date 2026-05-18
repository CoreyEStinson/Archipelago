import math
from typing import Dict, Any, List

from worlds.AutoWorld import World
from BaseClasses import Region, Location, Item

from .locations import location_table, LOOT_CHECK_BASE_ID, LOOT_CHECK_MAX

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

    item_name_to_id = {name: data.code for name, data in item_table.items()}

    location_name_to_id = {
        **{name: data.code for name, data in location_table.items()},
        **{f"Loot Check {i + 1}": LOOT_CHECK_BASE_ID + i
           for i in range(LOOT_CHECK_MAX)},
    }

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

        # Static advancement locations
        for loc_name, loc_data in location_table.items():
            target_region = region_map[loc_data.region]
            location = MinecraftArchipelagoLocation(
                self.player, loc_name, loc_data.code, target_region
            )
            target_region.locations.append(location)

        # Dynamic loot check locations — count set per player in YAML
        # All go in Overworld; no region gate (chests are accessible from the start)
        for i in range(self.options.loot_check_count.value):
            loc_name = f"Loot Check {i + 1}"
            location = MinecraftArchipelagoLocation(
                self.player, loc_name, LOOT_CHECK_BASE_ID + i, overworld
            )
            overworld.locations.append(location)

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

        total_locations = len(location_table) + self.options.loot_check_count.value

        # Fill any remaining slots with random filler items.
        # There are 112 locations and 39 important items, so we need 73 fillers.
        filler_pool = list(filler_items.keys())
        remaining = len(location_table) - len(pool)

        if total_locations < len(pool):
            raise Exception(
                f"Too many items ({len(pool)}) for available locations ({total_locations})"
            )

        # Fill every remaining slot from the filler pool.
        # This covers both the advancement remainder and all loot check slots —
        # the generator distributes them freely across all location types.
        filler_pool = list(filler_items.keys())
        remaining = total_locations - len(pool)
        for _ in range(remaining):
            pool.append(self.random.choice(filler_pool))

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
        apply_rules(self)

        # Matches the mod's integer math
        # mod checks: checked * 100 >= total * goalPercent
        # which is eqivelent to: checked >= ceil(total * goalPercent / 100)
        total = len(self.location_name_to_id)
        required = max(1, math.ceil(
            total * self.options.advancement_goal.value / 100
        ))

        def is_complete(state) -> bool:
            # Count reachable locations, short-circut as soon as target is hit.
            # Avoids checking all 112 locations every time this is evaluated.
            count = 0
            for loc_name in self.location_name_to_id:
                if state.can_reach(loc_name, "Location", self.player):
                    count += 1
                    if count >= required:
                        return True
            return False
        
        self.multiworld.completion_condition[self.player] = is_complete

    # ── Slot data ─────────────────────────────────────────────────────────

    def fill_slot_data(self) -> Dict[str, Any]:
        # This dict is sent to the mod on connect.
        # SlotData.java reads these values — key names must match exactly.
        return {
            "advancement_goal": self.options.advancement_goal.value,
            "loot_check_count": self.options.loot_check_count.value,
            "death_link": bool(self.options.death_link.value),
        }