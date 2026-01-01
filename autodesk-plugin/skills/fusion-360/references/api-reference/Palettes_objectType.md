# Palettes.objectType Property

Parent Object: [Palettes](Palettes.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Palettes.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"palettes\_var" is a variable referencing a Palettes object.  ```` ``` # Get the value of the property. propertyValue = palettes_var.objectType ``` ```` |

"palettes\_var" is a variable referencing a Palettes object. ```` ``` #include <Core/UserInterface/Palettes.h>  // Get the value of the property. string propertyValue = palettes_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |