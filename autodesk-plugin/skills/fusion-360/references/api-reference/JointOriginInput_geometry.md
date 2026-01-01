# JointOriginInput.geometry Property

Parent Object: [JointOriginInput](JointOriginInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOriginInput.h>

## Description

Gets and sets the joint geometry for this joint origin input. This defines the location of the joint origin.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOriginInput\_var" is a variable referencing a JointOriginInput object. |

"jointOriginInput\_var" is a variable referencing a JointOriginInput object. ```` ``` #include <Fusion/Components/JointOriginInput.h>  // Get the value of the property. Ptr<JointGeometry> propertyValue = jointOriginInput_var->geometry();  // Set the value of the property, where value_var is a JointGeometry. bool returnValue = jointOriginInput_var->geometry(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [JointGeometry](JointGeometry.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |