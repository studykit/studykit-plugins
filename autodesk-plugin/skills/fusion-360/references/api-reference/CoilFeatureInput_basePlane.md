# CoilFeatureInput.basePlane Property

Parent Object: [CoilFeatureInput](CoilFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CoilFeatureInput.h>

## Description

Gets and sets the base plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"coilFeatureInput\_var" is a variable referencing a CoilFeatureInput object. |

"coilFeatureInput\_var" is a variable referencing a CoilFeatureInput object. ```` ``` #include <Fusion/Features/CoilFeatureInput.h>  // Get the value of the property. Ptr<Base> propertyValue = coilFeatureInput_var->basePlane();  // Set the value of the property, where value_var is a Base. bool returnValue = coilFeatureInput_var->basePlane(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version March 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |