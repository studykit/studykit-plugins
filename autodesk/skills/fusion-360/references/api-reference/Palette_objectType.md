# Palette.objectType Property

Parent Object: [Palette](Palette.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palette.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palette\_var" is a variable referencing a Palette object.  ```` ``` # Get the value of the property. propertyValue = palette_var.objectType ``` ```` |

"palette\_var" is a variable referencing a Palette object. ```` ``` #include <Core/UserInterface/Palette.h>  // Get the value of the property. string propertyValue = palette_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |