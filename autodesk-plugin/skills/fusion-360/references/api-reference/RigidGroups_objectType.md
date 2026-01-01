# RigidGroups.objectType Property

Parent Object: [RigidGroups](RigidGroups.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroups.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroups\_var" is a variable referencing a RigidGroups object.  ```` ``` # Get the value of the property. propertyValue = rigidGroups_var.objectType ``` ```` |

"rigidGroups\_var" is a variable referencing a RigidGroups object. ```` ``` #include <Fusion/Components/RigidGroups.h>  // Get the value of the property. string propertyValue = rigidGroups_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |