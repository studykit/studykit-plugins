# Joints.objectType Property

Parent Object: [Joints](Joints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joints.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joints\_var" is a variable referencing a Joints object.  ```` ``` # Get the value of the property. propertyValue = joints_var.objectType ``` ```` |

"joints\_var" is a variable referencing a Joints object. ```` ``` #include <Fusion/Components/Joints.h>  // Get the value of the property. string propertyValue = joints_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |