# AsBuiltJoint.geometry Property

Parent Object: [AsBuiltJoint](AsBuiltJoint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJoint.h>

## Description

Specifies the position of the joint. Getting this property will return null and setting it will be ignored in the case where the joint motion is rigid.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJoint\_var" is a variable referencing an AsBuiltJoint object.  ```` ``` # Get the value of the property. propertyValue = asBuiltJoint_var.geometry  # Set the value of the property. asBuiltJoint_var.geometry = propertyValue ``` ```` |

"asBuiltJoint\_var" is a variable referencing an AsBuiltJoint object. ```` ``` #include <Fusion/Components/AsBuiltJoint.h>  // Get the value of the property. Ptr<JointGeometry> propertyValue = asBuiltJoint_var->geometry();  // Set the value of the property, where value_var is a JointGeometry. bool returnValue = asBuiltJoint_var->geometry(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [JointGeometry](JointGeometry.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |