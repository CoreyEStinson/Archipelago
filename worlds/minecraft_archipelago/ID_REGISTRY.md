# Minecraft Archipelago ID Registry

This file defines the ID ranges used by the Minecraft Archipelago world and mod.

Keep item IDs and location IDs in their assigned ranges. When adding something new, use the lowest unused ID in the appropriate range.

These IDs only need to be unique within Minecraft Archipelago. They do not conflict with IDs used by other Archipelago games.

## Item IDs

| Range | Use |
|---|---|
| 10000–10999 | Progressive items and progressive gifts |
| 11000–11999 | Item unlocks |
| 12000–12999 | Block unlocks |
| 13000–13999 | Gamerules |
| 14000–14999 | Filler items |

Progressive gifts belong in the progressive range.

An item unlock allows the player to use an item. A block unlock allows the player to use or place a block.

## Location IDs

| Range | Use |
|---|---|
| 20000–20999 | Advancement locations |
| 21000–21999 | Boss kill locations |
| 22000–22999 | Lootable check locations |
| 23000–23999 | Future check types |

Lootable checks have a full reserved range, even though the mod currently supports only 50 active lootable checks.

## Packages

Mod packages do not receive Archipelago IDs.

Packages are internal mod data that describe what an AP item gives the player. For example, one progressive gift item can grant a different package at each tier.

## When a range is full

Do not place an ID in another category’s range. Update this file and revise the layout before adding more IDs.