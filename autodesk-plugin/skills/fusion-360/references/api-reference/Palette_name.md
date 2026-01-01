# Palette.name Property

Parent Object: [Palette](Palette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palette.h>

## Description

Gets and set the name of the palette as seen in the user interface. The name of native palettes cannot be set.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palette\_var" is a variable referencing a Palette object. |

"palette\_var" is a variable referencing a Palette object. ```` ``` #include <Core/UserInterface/Palette.h>  // Get the value of the property. string propertyValue = palette_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = palette_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |