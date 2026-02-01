# JointGeometry.objectType Property

Parent Object: [JointGeometry](JointGeometry.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointGeometry.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointGeometry\_var" is a variable referencing a JointGeometry object.  ```` ``` # Get the value of the property. propertyValue = jointGeometry_var.objectType ``` ```` |

"jointGeometry\_var" is a variable referencing a JointGeometry object. ```` ``` #include <Fusion/Components/JointGeometry.h>  // Get the value of the property. string propertyValue = jointGeometry_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |