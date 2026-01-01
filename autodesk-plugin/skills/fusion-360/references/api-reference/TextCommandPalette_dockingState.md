# TextCommandPalette.dockingState Property

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

Gets and sets how the palette is currently docked.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textCommandPalette\_var" is a variable referencing a TextCommandPalette object. |

"textCommandPalette\_var" is a variable referencing a TextCommandPalette object. ```` ``` #include <Core/UserInterface/TextCommandPalette.h>  // Get the value of the property. PaletteDockingStates propertyValue = textCommandPalette_var->dockingState();  // Set the value of the property, where value_var is a PaletteDockingStates. bool returnValue = textCommandPalette_var->dockingState(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PaletteDockingStates](PaletteDockingStates.htm).

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |