# RigidJointMotion.objectType Property

Parent Object: [RigidJointMotion](RigidJointMotion.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidJointMotion.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidJointMotion\_var" is a variable referencing a RigidJointMotion object.  ```` ``` # Get the value of the property. propertyValue = rigidJointMotion_var.objectType ``` ```` |

"rigidJointMotion\_var" is a variable referencing a RigidJointMotion object. ```` ``` #include <Fusion/Components/RigidJointMotion.h>  // Get the value of the property. string propertyValue = rigidJointMotion_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |