# Palette.isNative Property

Parent Object: [Palette](Palette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palette.h>

## Description

Indicates if this is one of the standard Fusion palettes or a custom palette created through the API. If true, it is a standard Fusion palette and will have some restrictions on changing its properties and cannot be deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palette\_var" is a variable referencing a Palette object. |

"palette\_var" is a variable referencing a Palette object. ```` ``` #include <Core/UserInterface/Palette.h>  // Get the value of the property. boolean propertyValue = palette_var->isNative(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |