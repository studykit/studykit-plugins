# SymmetricExtentDefinition.objectType Property

Parent Object: [SymmetricExtentDefinition](SymmetricExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SymmetricExtentDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"symmetricExtentDefinition\_var" is a variable referencing a SymmetricExtentDefinition object.  ```` ``` # Get the value of the property. propertyValue = symmetricExtentDefinition_var.objectType ``` ```` |

"symmetricExtentDefinition\_var" is a variable referencing a SymmetricExtentDefinition object. ```` ``` #include <Fusion/Features/SymmetricExtentDefinition.h>  // Get the value of the property. string propertyValue = symmetricExtentDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |