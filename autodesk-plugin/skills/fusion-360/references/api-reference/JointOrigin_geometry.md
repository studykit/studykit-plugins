# JointOrigin.geometry Property

Parent Object: [JointOrigin](JointOrigin.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigin.h>

## Description

Gets and sets the joint geometry for this joint origin input. This defines the location of the joint origin.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigin\_var" is a variable referencing a JointOrigin object.  ```` ``` # Get the value of the property. propertyValue = jointOrigin_var.geometry  # Set the value of the property. jointOrigin_var.geometry = propertyValue ``` ```` |

"jointOrigin\_var" is a variable referencing a JointOrigin object. ```` ``` #include <Fusion/Components/JointOrigin.h>  // Get the value of the property. Ptr<JointGeometry> propertyValue = jointOrigin_var->geometry();  // Set the value of the property, where value_var is a JointGeometry. bool returnValue = jointOrigin_var->geometry(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [JointGeometry](JointGeometry.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |