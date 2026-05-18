from dataclasses import dataclass
from Options import Range, Toggle, DeathLink, PerGameCommonOptions

class AdvancementGoal(Range):
    """The percentage of advancements required to trigger the win condition.
    A higher value means you need to complete more of the game before winning."""
    display_name = "Advancement Goal"
    range_start = 1
    range_end = 100
    default = 70

class LootCheckCount(Range):
    """How many Archipelago check tokens are seeded into structure chests.
    Set to 0 to disable loot checks entierly."""
    display_name = "Loot Check Count"
    range_start = 0
    range_end = 50
    default = 10

class DeathLink(DeathLink): # type: ignore
    """When you die, everyone dies. Of course the reverse is true too.
    Enable this if you want to share the pain with other players."""
    default = 0 # off by default

@dataclass
class MinecraftArchipelagoOptions(PerGameCommonOptions):
    advancement_goal: AdvancementGoal
    loot_check_count: LootCheckCount
    death_link : DeathLink