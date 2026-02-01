# AngleExtentDefinition.objectType Property

Parent Object: [AngleExtentDefinition](AngleExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/AngleExtentDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"angleExtentDefinition\_var" is a variable referencing an AngleExtentDefinition object.  ```` ``` # Get the value of the property. propertyValue = angleExtentDefinition_var.objectType ``` ```` |

"angleExtentDefinition\_var" is a variable referencing an AngleExtentDefinition object. ```` ``` #include <Fusion/Features/AngleExtentDefinition.h>  // Get the value of the property. string propertyValue = angleExtentDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |