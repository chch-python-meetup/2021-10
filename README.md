# Python Coding Challenge - Oct 2021

## The Challenge

[Zork](https://www.mentalfloss.com/article/29885/eaten-grue-brief-history-zork)
is a classic text adventure game created around 1977. We are going to
implement a basic Zork-like game engine using data from the original game. 

The game was original written in a language called MDL and then converted to
ZIL. Fortunately, JSON versions of the game data have been created and published on Github. The room
data is available [here](https://github.com/zork-playground/zil-to-json/blob/780cdde63e68e7190bcd2280177229c52efc0132/data/zork1/zork1.rooms.json).

Write a program that uses this to accept movement commands (e.g. "north",
"east", "southwest") to allow movement around the rooms from the original Zork
game. Be sure to handle directions which are defined but don't lead anywhere
(e.g. "The door is boarded and you can't remove the boards.").

Print out the description and long description (if any) of each room when the
player enters it.

## Extension Challenges

Once you have basic movement working, take the game further. Some ideas:

- Support aliases for movement directions (e.g. "n", "e", "sw")
- Add support for the "brief", "superbrief" and "verbose" commands.
- Add support for other commands.
- Add support for objects or other game aspects such as objects. See the [other
  JSON files](https://github.com/zork-playground/zil-to-json/tree/main/data/zork1).

A list of Zork commands can be found here: https://zork.fandom.com/wiki/Command_List

