# Palette.top Property

Parent Object: [Palette](Palette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palette.h>

## Description

Gets and sets the top of the palette relative to screen space and in pixels. Because palettes can be positioned outside of the Fusion window, a value of zero indicates the top of the screen and not the Fusion window.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palette\_var" is a variable referencing a Palette object. |

"palette\_var" is a variable referencing a Palette object. ```` ``` #include <Core/UserInterface/Palette.h>  // Get the value of the property. integer propertyValue = palette_var->top();  // Set the value of the property, where value_var is an integer. bool returnValue = palette_var->top(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |