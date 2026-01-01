# TextCommandPalette.width Property

Parent Object: [TextCommandPalette](TextCommandPalette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TextCommandPalette.h>

## Description

Gets and sets the width of the palette. Setting this property may not always set the width. Depending on how the palette is docked or snapped, the width may not be editable.

## Syntax

* [Python](#Python)
* [C++](#C++)

"textCommandPalette\_var" is a variable referencing a TextCommandPalette object. |

"textCommandPalette\_var" is a variable referencing a TextCommandPalette object. ```` ``` #include <Core/UserInterface/TextCommandPalette.h>  // Get the value of the property. integer propertyValue = textCommandPalette_var->width();  // Set the value of the property, where value_var is an integer. bool returnValue = textCommandPalette_var->width(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version August 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |