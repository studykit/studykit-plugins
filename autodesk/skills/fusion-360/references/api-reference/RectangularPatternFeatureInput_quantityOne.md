# RectangularPatternFeatureInput.quantityOne Property

Parent Object: [RectangularPatternFeatureInput](RectangularPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeatureInput.h>

## Description

Gets and sets the number of instances in the first direction.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeatureInput\_var" is a variable referencing a RectangularPatternFeatureInput object. |

"rectangularPatternFeatureInput\_var" is a variable referencing a RectangularPatternFeatureInput object. ```` ``` #include <Fusion/Features/RectangularPatternFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = rectangularPatternFeatureInput_var->quantityOne();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = rectangularPatternFeatureInput_var->quantityOne(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |