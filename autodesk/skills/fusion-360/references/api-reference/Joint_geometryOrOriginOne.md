# Joint.geometryOrOriginOne Property

Parent Object: [Joint](Joint.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joint.h>

## Description

Gets and sets the first JointGeometry or JointOrigin for this joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joint\_var" is a variable referencing a Joint object.  ```` ``` # Get the value of the property. propertyValue = joint_var.geometryOrOriginOne  # Set the value of the property. joint_var.geometryOrOriginOne = propertyValue ``` ```` |

"joint\_var" is a variable referencing a Joint object. ```` ``` #include <Fusion/Components/Joint.h>  // Get the value of the property. Ptr<Base> propertyValue = joint_var->geometryOrOriginOne();  // Set the value of the property, where value_var is a Base. bool returnValue = joint_var->geometryOrOriginOne(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |