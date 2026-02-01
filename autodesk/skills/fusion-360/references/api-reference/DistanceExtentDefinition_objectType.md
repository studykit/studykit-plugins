# DistanceExtentDefinition.objectType Property

Parent Object: [DistanceExtentDefinition](DistanceExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceExtentDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceExtentDefinition\_var" is a variable referencing a DistanceExtentDefinition object.  ```` ``` # Get the value of the property. propertyValue = distanceExtentDefinition_var.objectType ``` ```` |

"distanceExtentDefinition\_var" is a variable referencing a DistanceExtentDefinition object. ```` ``` #include <Fusion/Features/DistanceExtentDefinition.h>  // Get the value of the property. string propertyValue = distanceExtentDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |