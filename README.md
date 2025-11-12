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

---

# 📝 Addendum

## 🔄 Game compatibility
This mod has been tested with `The Sims 4` 1.119.109, S4CL 3.17, TS4Lib 0.3.42.
It is expected to remain compatible with future releases of TS4, S4CL, and TS4Lib.

## 📦 Dependencies
Download the ZIP file - not the source code.
Required components:
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

If not already installed, download and install TS4 and the listed mods. All are available for free.

## 📥 Installation
* Locate the localized `The Sims 4` folder (it contains the `Mods` folder).
* Extract the ZIP file directly into this folder.

This will create:
* `Mods/_o19_/$mod_name.ts4script`
* `Mods/_o19_/$mod_name.package`
* `mod_data/$mod_name/*`
* `mod_documentation/$mod_name/*` (optional)
* `mod_sources/$mod_name/*` (optional)

Additional notes:
* CAS and Build/Buy UGC without scripts will create `Mods/o19/$mod_name.package`.
* A log file `mod_logs/$mod_name.txt` will be created once data is logged.
* You may safely delete `mod_documentation/` and `mod_sources/` folders if not needed.

### 📂 Manual Installation
If you prefer not to extract directly into `The Sims 4`, you can extract to a temporary location and copy files manually:
* Copy `mod_data/` contents to `The Sims 4/mod_data/` (usually required).
* `mod_documentation/` is for reference only — not required.
* `mod_sources/` is not needed to run the mod.
* `.ts4script` files can be placed in a folder inside `Mods/`, but storing them in `_o19_` is recommended for clarity.
* `.package` files can be placed in a anywhere inside `Mods/`.

## 🛠️ Troubleshooting
If installed correctly, no troubleshooting should be necessary.
For manual installs, verify the following:
* Does your localized `The Sims 4` folder exist? (e.g. localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...)
  * Does it contain a `Mods/` folder?
    * Does Mods/_o19_/ contain:
      * `ts4lib.ts4script` and `ts4lib.package`?
      * `{mod_name}.ts4script` and/or `{mod_name}.package`
* Does `mod_data/` contain `{mod_name}/` with files?
* Does `mod_logs/` contain:
  * `Sims4CommunityLib_*_Messages.txt`?
  * `TS4-Library_*_Messages.txt`?
  * `{mod_name}_*_Messages.txt`?
* Are there any `last_exception.txt` or `last_exception*.txt` files in `The Sims 4`?


* When installed properly this is not necessary at all.
For manual installations check these things and make sure each question can be answered with 'yes'.
* Does 'The Sims 4' (localized to Die Sims 4, Les Sims 4, Los Sims 4, The Sims 4, ...) exist?
  * Does `The Sims 4` contain the folder `Mods`?
    * Does `Mods` contain the folder `_o19_`? 
      * Does `_19_` contain `ts4lib.ts4script` and `ts4lib.package` files?
      * Does `_19_` contain `{mod_name}.ts4script` and/or `{mod_name}.package` files?
  * Does `The Sims 4` contain the folder `mod_data`?
    * Does `mod_data` contain the folder `{mod_name}`?
      * Does `{mod_name}` contain files or folders?
  * Does `The Sims 4` contain the `mod_logs` ?
    * Does `mod_logs` contain the file `Sims4CommunityLib_*_Messages.txt`?
    * Does `mod_logs` contain the file `TS4-Library_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
    * Does `mod_logs` contain the file `{mod_name}_*_Messages.txt`?
      * Is this the most recent version or can it be updated?
  * Doesn't `The Sims 4` contain the file(s) `last_exception.txt`  and/or `last_exception*.txt` ?
* Share the `The Sims 4/mod_logs/Sims4CommunityLib_*_Messages.txt` and `The Sims 4/mod_logs/{mod_name}_*_Messages.txt`  file.

If issues persist, share:
`mod_logs/Sims4CommunityLib_*_Messages.txt`
`mod_logs/{mod_name}_*_Messages.txt`

## 🕵️ Usage Tracking / Privacy
This mod does not send any data to external servers.
The code is open source, unobfuscated, and fully reviewable.

Note: Some log entries (especially warnings or errors) may include your local username if file paths are involved.
Share such logs with care.

## 🔗 External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## ⚖️ Copyright and License
* © 2020-2025 [Oops19](https://github.com/Oops19)
* `.package` files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* All other content (unless otherwise noted): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 

You may use and adapt this mod and its code — even without owning The Sims 4.
Have fun extending or integrating it into your own mods!

Oops19 / o19 is not affiliated with or endorsed by Electronic Arts or its licensors.
Game content and materials © Electronic Arts Inc. and its licensors.
All trademarks are the property of their respective owners.

## 🧾 Terms of Service
* Do not place this mod behind a paywall.
* Avoid creating mods that break with every TS4 update.
* For simple tuning mods, consider using:
  * [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
  * [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To verify custom tuning structures, use:
  * [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).

## 🗑️ Removing the Mod
Installing this mod creates files in several directories. To fully remove it, delete:
* `The Sims 4/Mods/_o19_/$mod_name.*`
* `The Sims 4/mod_data/_o19_/$mod_name/`
* `The Sims 4/mod_documentation/_o19_/$mod_name/`
* `The Sims 4/mod_sources/_o19_/$mod_name/`

To remove all of my mods, delete the following folders:
* `The Sims 4/Mods/_o19_/`
* `The Sims 4/mod_data/_o19_/`
* `The Sims 4/mod_documentation/_o19_/`
* `The Sims 4/mod_sources/_o19_/`
