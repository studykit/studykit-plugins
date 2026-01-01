# Joint.isLocked Property

Parent Object: [Joint](Joint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Gets and sets if the joint is locked.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a Joint object. |

"joint\_var" is a variable referencing a Joint object. ```` ``` #include <Fusion/Components/Joint.h>  // Get the value of the property. boolean propertyValue = joint_var->isLocked();  // Set the value of the property, where value_var is a boolean. bool returnValue = joint_var->isLocked(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Joint API Sample](JointSample_Sample.htm) | Demonstrates creating a new joint. |

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |