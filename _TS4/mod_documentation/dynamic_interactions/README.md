# Dynamic Interactions

This mod is meant to alter the game play and give objects new interactions or remove some.

It's based on a quite an old mod of mine 'Copy Interactions' which I never released while I used it to copy 'clutter' interactions to objects to make them behave like clutter.

It allows to add and remove interactions to objects based on the neighbourhood, lot, room and other objects.

The mod is fed with configuration files and allows to customize how objects behave.

## Cheat commands
* `o19.dynint.init` Read and apply the configuration files after modifying them.
* `o19.dynint.info` Log and print lot information for the current active sim.

## Don't Wash Dishes Where You Angry Poop
Scumbumbo did a good job when writing [Don't Wash Dishes Where You Angry Poop](https://modthesims.info/d/603052/don-t-wash-dishes-where-you-angry-poop.html).
This was very likely the best implementation which was possible back then.
Overriding TS4 tunings and adding new tests to interactions which are not needed at all is very questionable and in the long term his mod broke.

From my point of view one should keep it simple and instead of creating workarounds by adding tests to interactions one should fix the root cause and remove the offending interactions.
With no interaction sim's will not use such objects.

That's what this mod does when reading the 'DontWashDishesWhereYouAngryPoop.txt' file.
It looks for sinks and if a toilet is in the same room then some interactions will be removed from the sink.

In December 2023 EA added the 'Set Sink Type ...' interaction to all sinks so one can manage this manually.

## Don't Brush Your Teeth in Kitchen
Basically a clone of the configuration file to 'DontBrushTeethInKitchen.txt'.
As soon as a `Fridge` or `Oven` is in the room a few interactions which are not appropriate for the kitchen will be removed.

## Batuu
In 'Oga´s Cantina' there are six bars.
As this place is never crowded it makes sense to disable at least some of them.
The included 'Disable_Batuu_Bars.txt' file disables all but the two rounded bars at the entrance.
Barkeepers may need some time to use the right bar.

## More
That's all folks.
One could modify toilets and remove the 'toilet-use-standing (14428)' and/or 'toilet_Toddler_PlayIn (155887)' interactions.
Also, the 'art_View (33623)' interactions can be added to most objects.

Adding random interactions to random objects will often fail with a routing error.
A table has different bones than a bed and one can't simply exchange the tunings as they animations will fail.

For large builds one can use this mod to disable object interactions for various objects. 
If there are 3 bedrooms and only one should be used one can disable the 'sleep' interactions.

### Creating Custom Configuration Files
* Use 'Sims 4 Community Library ...' > 'Log All Game Tags'  to log the game tags.
* Use the S4CL debug menu 'Sims 4 Community Library ...' > 'Log All Interactions' to log the object name and interactions to the S4CL log file.

The `o19.dynint.info` command will log the world, lot and block id for the active sim.
Changing the room will result in a different block_id.

These options should log enough information to create custom configuration files. The files look a lot like JSON while they are Python Dict objects.

### Future
#### Completeness of Vision vs. Ability to Execute
All these things are not yet implemented. I'm not sure if I will ever add them.
* Specify strings for 'CommonGameTag' instead of numbers.
* Specify strings for interactions instead of numbers.
* 'set_interactions': Completely replace interactions instead of 'add_' and 'remove_'
* 'add/remove/set_posture_families'
* 'add/remove/set_tags': Add tags like unbreakable to an object
* 'set_broken': Repair / break objects
* 'copy/paste': Paste interactions from random objects


# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.111.102, S4CL 3.9, TS4Lib 0.3.33.
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
Download the ZIP file, not the sources.
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not installed download and install TS4 and these mods.
All are available for free.

## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*`
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this. 
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2024 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
