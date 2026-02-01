# TextCommandPalette.dockingOption Property

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

Defines the docking behavior for this palette. This controls how the user is allowed to dock the palette.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textCommandPalette\_var" is a variable referencing a TextCommandPalette object. |

"textCommandPalette\_var" is a variable referencing a TextCommandPalette object. ```` ``` #include <Core/UserInterface/TextCommandPalette.h>  // Get the value of the property. PaletteDockingOptions propertyValue = textCommandPalette_var->dockingOption();  // Set the value of the property, where value_var is a PaletteDockingOptions. bool returnValue = textCommandPalette_var->dockingOption(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PaletteDockingOptions](PaletteDockingOptions.htm).

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |