# SphereFeatures.objectType Property

Parent Object: [SphereFeatures](SphereFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SphereFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sphereFeatures\_var" is a variable referencing a SphereFeatures object.  ```` ``` # Get the value of the property. propertyValue = sphereFeatures_var.objectType ``` ```` |

"sphereFeatures\_var" is a variable referencing a SphereFeatures object. ```` ``` #include <Fusion/Features/SphereFeatures.h>  // Get the value of the property. string propertyValue = sphereFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |