# Palette.dockingOption Property

Parent Object: [Palette](Palette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palette.h>

## Description

Defines the docking behavior for this palette. This controls how the user is allowed to dock the palette.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palette\_var" is a variable referencing a Palette object. |

"palette\_var" is a variable referencing a Palette object. ```` ``` #include <Core/UserInterface/Palette.h>  // Get the value of the property. PaletteDockingOptions propertyValue = palette_var->dockingOption();  // Set the value of the property, where value_var is a PaletteDockingOptions. bool returnValue = palette_var->dockingOption(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PaletteDockingOptions](PaletteDockingOptions.htm).

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |