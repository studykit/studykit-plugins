# Joint.isFlipped Property

Parent Object: [Joint](Joint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Gets and sets if the joint direction is flipped or not. This is effectively specifying if the third axis of the two input geometries is facing (false) or opposed (true).

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a Joint object.  ```` ``` # Get the value of the property. propertyValue = joint_var.isFlipped  # Set the value of the property. joint_var.isFlipped = propertyValue ``` ```` |

"joint\_var" is a variable referencing a Joint object. ```` ``` #include <Fusion/Components/Joint.h>  // Get the value of the property. boolean propertyValue = joint_var->isFlipped();  // Set the value of the property, where value_var is a boolean. bool returnValue = joint_var->isFlipped(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |