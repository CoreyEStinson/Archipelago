from dataclasses import dataclass
from Options import Range, Toggle, DeathLink, PerGameCommonOptions, OptionSet

class AdvancementGoal(Range):
    """Percentage of advancements required to meet the advancement win condition.
    Set to 0 to disable the advancement goal entirely.
    At least one win condition must be active."""
    display_name = "Advancement Goal"
    range_start = 0 # 0 = disbled
    range_end = 100
    default = 70


class DeathLink(DeathLink): # type: ignore
    """When you die, everyone dies. Of course the reverse is true too.
    Enable this if you want to share the pain with other players."""
    default = 0 # off by default


class LootableChecks(Range):
    """How many Archipelago Loot items are hidden in structure chests.
    Each one is a location check. 
    Set to 0 to disable lootable checks."""
    display_name = "Lootable Checks"
    range_start = 0
    range_end = 41
    default = 20


class RequiredLootableChecks(Range):
    """How many Archipelago Loot items must be claimed to meet the lootable
    checks win condition. Set to 0 to disable. Cannot exceed Lootable Checks."""
    display_name = "Required Lootable Checks"
    range_start  = 0
    range_end    = 42
    default      = 0


class RequiredBossKills(OptionSet):
    """Which bosses must be killed to satisfy the boss kill win condition.
    Leave empty to disable boss kills as a win condition entirely.
    Boss kill locations exist in the item pool regardless of this setting.
    
    Valid values: ender_dragon, wither, elder_guardian, warden"""
    display_name = "Required Boss Kills"
    valid_keys = {"ender_dragon", "wither", "elder_guardian", "warden"}
    default = frozenset()


@dataclass
class MinecraftArchipelagoOptions(PerGameCommonOptions):
    advancement_goal: AdvancementGoal
    death_link: DeathLink
    lootable_checks: LootableChecks
    required_lootable_checks: RequiredLootableChecks
    required_boss_kills: RequiredBossKills