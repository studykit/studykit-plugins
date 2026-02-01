# LoftSmoothEndCondition.weight Property

Parent Object: [LoftSmoothEndCondition](LoftSmoothEndCondition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftSmoothEndCondition.h>

## Description

Gets the valueInput or Parameter that defines the weight of the loft. If this object was obtained from a LoftFeatureInput object then this will return a valueInput object with the initial value provided. If this object was obtained from an exiting LoftFeature then it returns a Parameter. In the case of a parameter, to change the weight, edit the value of the associated parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftSmoothEndCondition\_var" is a variable referencing a LoftSmoothEndCondition object. |

"loftSmoothEndCondition\_var" is a variable referencing a LoftSmoothEndCondition object. ```` ``` #include <Fusion/Features/LoftSmoothEndCondition.h>  // Get the value of the property. Ptr<Base> propertyValue = loftSmoothEndCondition_var->weight(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |