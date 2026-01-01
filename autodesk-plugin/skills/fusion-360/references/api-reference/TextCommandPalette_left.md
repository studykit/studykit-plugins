# TextCommandPalette.left Property

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

Gets and sets the left side of the palette relative to screen space and in pixels. Because palettes can be positioned outside of the Fusion window, a value of zero indicates the left side of the screen and not the Fusion window.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textCommandPalette\_var" is a variable referencing a TextCommandPalette object. |

"textCommandPalette\_var" is a variable referencing a TextCommandPalette object. ```` ``` #include <Core/UserInterface/TextCommandPalette.h>  // Get the value of the property. integer propertyValue = textCommandPalette_var->left();  // Set the value of the property, where value_var is an integer. bool returnValue = textCommandPalette_var->left(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |