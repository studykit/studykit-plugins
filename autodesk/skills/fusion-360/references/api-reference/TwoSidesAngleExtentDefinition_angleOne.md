# TwoSidesAngleExtentDefinition.angleOne Property

Parent Object: [TwoSidesAngleExtentDefinition](TwoSidesAngleExtentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TwoSidesAngleExtentDefinition.h>

## Description

Gets the ModelParameter that defines the angle on the first side. The value of the angle can be edited by using the properties on the ModelParameter object to edit the parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"twoSidesAngleExtentDefinition\_var" is a variable referencing a TwoSidesAngleExtentDefinition object. |

"twoSidesAngleExtentDefinition\_var" is a variable referencing a TwoSidesAngleExtentDefinition object. ```` ``` #include <Fusion/Features/TwoSidesAngleExtentDefinition.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = twoSidesAngleExtentDefinition_var->angleOne(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |