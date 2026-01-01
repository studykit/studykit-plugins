# DistanceAndAngleChamferTypeDefinition.objectType Property

Parent Object: [DistanceAndAngleChamferTypeDefinition](DistanceAndAngleChamferTypeDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DistanceAndAngleChamferTypeDefinition.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"distanceAndAngleChamferTypeDefinition\_var" is a variable referencing a DistanceAndAngleChamferTypeDefinition object.  ```` ``` # Get the value of the property. propertyValue = distanceAndAngleChamferTypeDefinition_var.objectType ``` ```` |

"distanceAndAngleChamferTypeDefinition\_var" is a variable referencing a DistanceAndAngleChamferTypeDefinition object. ```` ``` #include <Fusion/Features/DistanceAndAngleChamferTypeDefinition.h>  // Get the value of the property. string propertyValue = distanceAndAngleChamferTypeDefinition_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |