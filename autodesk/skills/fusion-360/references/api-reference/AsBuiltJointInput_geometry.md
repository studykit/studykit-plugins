# AsBuiltJointInput.geometry Property

Parent Object: [AsBuiltJointInput](AsBuiltJointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJointInput.h>

## Description

Specifies the position of the joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJointInput\_var" is a variable referencing an AsBuiltJointInput object. |

"asBuiltJointInput\_var" is a variable referencing an AsBuiltJointInput object. ```` ``` #include <Fusion/Components/AsBuiltJointInput.h>  // Get the value of the property. Ptr<JointGeometry> propertyValue = asBuiltJointInput_var->geometry();  // Set the value of the property, where value_var is a JointGeometry. bool returnValue = asBuiltJointInput_var->geometry(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [JointGeometry](JointGeometry.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |