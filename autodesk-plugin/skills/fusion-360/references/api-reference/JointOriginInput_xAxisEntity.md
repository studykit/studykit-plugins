# JointOriginInput.xAxisEntity Property

Parent Object: [JointOriginInput](JointOriginInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOriginInput.h>

## Description

Gets and sets the entity that defines the X axis direction. This defaults to null meaning the X axis is inferred from the input geometry.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOriginInput\_var" is a variable referencing a JointOriginInput object. |

"jointOriginInput\_var" is a variable referencing a JointOriginInput object. ```` ``` #include <Fusion/Components/JointOriginInput.h>  // Get the value of the property. Ptr<Base> propertyValue = jointOriginInput_var->xAxisEntity();  // Set the value of the property, where value_var is a Base. bool returnValue = jointOriginInput_var->xAxisEntity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |