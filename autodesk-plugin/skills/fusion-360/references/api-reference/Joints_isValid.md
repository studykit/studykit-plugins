# Joints.isValid Property

Parent Object: [Joints](Joints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joints.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joints\_var" is a variable referencing a Joints object. |

"joints\_var" is a variable referencing a Joints object. ```` ``` #include <Fusion/Components/Joints.h>  // Get the value of the property. boolean propertyValue = joints_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |