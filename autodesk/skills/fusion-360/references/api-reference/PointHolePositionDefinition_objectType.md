# PointHolePositionDefinition.objectType Property

Parent Object: [PointHolePositionDefinition](PointHolePositionDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PointHolePositionDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pointHolePositionDefinition\_var" is a variable referencing a PointHolePositionDefinition object.  ```` ``` # Get the value of the property. propertyValue = pointHolePositionDefinition_var.objectType ``` ```` |

"pointHolePositionDefinition\_var" is a variable referencing a PointHolePositionDefinition object. ```` ``` #include <Fusion/Features/PointHolePositionDefinition.h>  // Get the value of the property. string propertyValue = pointHolePositionDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |