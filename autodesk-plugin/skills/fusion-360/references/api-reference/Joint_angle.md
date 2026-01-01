# Joint.angle Property

Parent Object: [Joint](Joint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Returns the parameter controlling the angle between the two input geometries. This is effectively the angle between the two primary axes of the two joint geometries.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a Joint object.  ```` ``` # Get the value of the property. propertyValue = joint_var.angle ``` ```` |

"joint\_var" is a variable referencing a Joint object. ```` ``` #include <Fusion/Components/Joint.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = joint_var->angle(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |