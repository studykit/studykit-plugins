# ToEntityExtentDefinition.objectType Property

Parent Object: [ToEntityExtentDefinition](ToEntityExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ToEntityExtentDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object.  ```` ``` # Get the value of the property. propertyValue = toEntityExtentDefinition_var.objectType ``` ```` |

"toEntityExtentDefinition\_var" is a variable referencing a ToEntityExtentDefinition object. ```` ``` #include <Fusion/Features/ToEntityExtentDefinition.h>  // Get the value of the property. string propertyValue = toEntityExtentDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |