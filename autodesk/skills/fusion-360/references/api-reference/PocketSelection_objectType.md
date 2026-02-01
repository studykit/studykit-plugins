# PocketSelection.objectType Property

Parent Object: [PocketSelection](PocketSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/PocketSelection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pocketSelection\_var" is a variable referencing a PocketSelection object.  ```` ``` # Get the value of the property. propertyValue = pocketSelection_var.objectType ``` ```` |

"pocketSelection\_var" is a variable referencing a PocketSelection object. ```` ``` #include <Cam/GeometrySelections/PocketSelection.h>  // Get the value of the property. string propertyValue = pocketSelection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |