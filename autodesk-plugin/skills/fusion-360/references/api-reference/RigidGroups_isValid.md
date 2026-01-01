# RigidGroups.isValid Property

Parent Object: [RigidGroups](RigidGroups.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroups.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroups\_var" is a variable referencing a RigidGroups object. |

"rigidGroups\_var" is a variable referencing a RigidGroups object. ```` ``` #include <Fusion/Components/RigidGroups.h>  // Get the value of the property. boolean propertyValue = rigidGroups_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |