# JointInput.geometryOrOriginTwo Property

Parent Object: [JointInput](JointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointInput.h>

## Description

Gets and sets the second JointGeometry or JointOrigin for this joint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointInput\_var" is a variable referencing a JointInput object. |

"jointInput\_var" is a variable referencing a JointInput object. ```` ``` #include <Fusion/Components/JointInput.h>  // Get the value of the property. Ptr<Base> propertyValue = jointInput_var->geometryOrOriginTwo();  // Set the value of the property, where value_var is a Base. bool returnValue = jointInput_var->geometryOrOriginTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |