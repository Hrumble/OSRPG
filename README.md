This project is an open source python RPG
Feel free to download it, toy with the code, add biome, items, entities, and anything you can think of.
keep reading to get a tutorial on adding anything in the game as it is.

=================ADDING=ITEMS====================

This one is pretty straightforward

1. Open WorldRegistry.py

2. Go under "#Items# id, name, value"

3. Below all the already existing items add

```python
    ITEM_REGISTRY.AddToRegistry(Item("item_id", "Item Name", value))
```

4. Replace item_id by your item's ID, Item Name by your item's name, and the value by your
desired value

5. Adding a "Mushroom Spore" Item with a price of 10 would look like:

```python
    ITEM_REGISTRY.AddToRegistry(Item("mushroom_spore", "Mushroom Spore", 10))
```

=================================================

================Adding=Consumables===============

Pretty much as easy

1. Open WorldRegistry.py

2. Go under "#Consumables"

3. Below all the already existing items add

```python
    ITEM_REGISTRY.AddToRegistry(ConsumableItem("consumable_id", "Consumable Name", value, health_modifier, craftable))
```

4. replace everything like with the item:

```
    health_modifier = value between 0 and 1 to indicate how much the consumable heals
    craftable = True or False on whether or not the item is craftable
```

5. !CAUTION! if craftable is set to True, you MUST add a recipe. (See below on how to add recipes)

=================================================

================Adding=Recipes===================

Recipes are in json format, and must be placed in the RPG/CraftingRecipes/ folder

1. go in the RPG/CraftingRecipes/ folder

2. create a new json file with the name of the item's id
(if you wanted to add a recipe for the Mushroom Spore it would be : mushroom_spore.json)

3. In the json file, add:

```json
{
  "materials" : {
    "material_1" : quantity1,
    "material_2" : quantity2,
    "material_3" : quantity3
  }
}
```

4. of course replace all the values with your desired values, add as much materials as you want.
Here is an example of a file called wolf_sword.json:

```json
{
  "materials" : {
    "wolf_fang" : 3,
    "sturdy_iron_sword" : 1
  }
}
```

this item requires 3 Wolf fangs and 1 Sturdy Iron Sword to be crafted

5. Save the json file.

=================================================

================Adding=Weapons===================

1. in WorldRegistry.py go under all the existing weapons under #Weapons

2. add this line:

```python
    ITEM_REGISTRY.AddToRegistry(WeaponItem("weapon_id", "Weapon Name", value, damage))
```

3. Replace with your desired values

4. For damage, most beginner enemies have around 10hp which should give you a good idea of the damage scale.
(damage=10 would one shot the enemy)

=================================================

================Adding=Armor=====================

1. in WorldRegistry.py go under all the existing armor items under #Armor

2. Add this line:

```python
    ITEM_REGISTRY.AddToRegistry(ArmorItem("armor_id", "Armor Name", value, protection, ArmorItem.slot_name))
```

3. There are 4 total possible slots:

```
    ArmorItem.headSlot
    ArmorItem.chestSlot
    ArmorItem.legSlot
    ArmorItem.feetSlot
```

=================================================

================Adding=Loot=Tables===============
!THIS IS OUTDATED!
The loots tables don't work like that anymore, they work with json files. (I'll update the README soon in the meantime
refer to OSRPG/LootTables/ to find the current loot tables and try understanding for yourself)

1. In WorldRegistry.py go under all the existing tables under #Loot Tables

2. Add this line:

```python
    enemy_id_table = LootTable(["item_id_1", "item_id_2"], [quantity_of_item1, quantity_of_item2], [dropchance_item1,
    dropchance_item2])
```

3. Replace all the values. add as much items and quantities as you want.

Here is an example of the slime's loot table
    slime_table = LootTable(["slimeball", "apple"], [2, 1], [100, 25])
(Slime has a 100% chance of dropping 2 slimeballs and 25% chance of dropping 1 apple)

=================================================

================Adding=Enemies==================

1. In WorldRegistry.py go under all the existing entities under #Entities

2. Add this line:

```python
    ENTITY_REGISTRY.AddToRegistry(Enemy("enemy_id", "Enemy Name", baseHealth, baseDamage, enemy_id_table))
```

3. Replace all the values, baseHealth and baseDamage is just the health and damage of the enemy

Here an example of the slime enemy:

```python
    ENTITY_REGISTRY.AddToRegistry(Enemy("slime", "Slime", 10, 2, slime_table))
```

=================================================

================Adding=Traders===================

1. In WorldRegistry.py go under all the existing entities under #Entities

2. Add this line:

```python
    ENTITY_REGISTRY.AddToRegistry(Trader("trader_id", "Trader Name", resale_rate,
                                     ["item_id_1", "item_id_2", "item_id_3", "item_id_4"],
                                     [quantity1, quantity2, quantity3, quantity4]))
```

3. Replace all the values and add as many items and quantities as you want

4. resale_rate is the price at which the trader will sell you items based on their values.
    a resale rate of 1 would make that trader sell you items at the same price that you sold them to him

Here is the example of a Wandering Trader:

```python
    ENTITY_REGISTRY.AddToRegistry(Trader("wandering_trader", "Wandering Trader", 1.5,
                                     ["leather_helmet", "leather_leggings", "pie", "small_potion"],
                                     [2, 1, 10, 6]))
```

=================================================

================Adding=Biomes====================
1. In WorldLoc.py go under all the existing biomes under #Biomes

2. Add this line:

```python
    BIOMES.append(Biome("Biome Name", [initial_X_position, initial_Y_position],
    biome_radius, ["enemy_id1", "enemy_id2", "enemy_id3", "enemy_id4"], enemy_level, enemy_effective))
```

3. Replace all the values, here is a quick explanation of some of them:

```
    enemy_level = the level around which the enemies will be inside the biome
    enemy_effective = How much enemies are in the biome
    [initial_X_position, initial_Y_position] = the position of the center of the biome
    biome_radius = How much the biome extends beyond its center
```

Here is an example of the starting biome
```python
    BIOMES.append(Biome("Starter Plains", [0, 0],
    10, ["slime", "spider", "wolf", "wandering_trader"], 0, 60))
```
The biome is centered at 0 0 and makes a square going from [-10, -10] to [10, 10]
It contains a total of 60 slimes + spiders + wolves + wandering traders each of level 0.

=================================================

With all of this you should be good to go to add pretty much anything into the game.
Check out the entire code to get a better grasp of it, and be able to add
your own entity classes and weapons and so on.