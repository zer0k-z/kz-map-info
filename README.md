# CS:GO KZ Maps Information

## Description

This repository contains a JSON file which contains information about all global maps: map ID, map name, difficulty, mapper name and steamid64 (if exists).

Current global maps with mapper name missing: kz_de_bhop, kz_tron_global.

The forum post can be found [here](https://forum.gokz.org/d/2052-making-it-easier-to-find-mappers).
The original spreadsheet can be found [here](https://docs.google.com/spreadsheets/d/1B11jVyb0KneTQWIx-jKgnZ9LL9bOLzRatP6SIhDC9UE/edit?usp=sharing).

## Contributing

If you would like to add information about missing global maps or fix incorrect information, feel free to make a fork of this repository and create a pull request from your fork to this repo.

The JSON format for a map looks like this:

```json
   {
      "id":"123",
      "name":"kz_map",
      "difficulty":"1",
      "workshop_url":"https://steamcommunity.com/sharedfiles/filedetails/?id=1234567890",
      "mapper_name":"mapper name",
      "mapper_steamid64":"76561198118681904"
   }
```
