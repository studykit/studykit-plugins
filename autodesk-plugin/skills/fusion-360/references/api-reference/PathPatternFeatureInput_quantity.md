# PathPatternFeatureInput.quantity Property

Parent Object: [PathPatternFeatureInput](PathPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeatureInput.h>

## Description

Gets and sets quantity of the elements.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeatureInput\_var" is a variable referencing a PathPatternFeatureInput object. |

"pathPatternFeatureInput\_var" is a variable referencing a PathPatternFeatureInput object. ```` ``` #include <Fusion/Features/PathPatternFeatureInput.h>  // Get the value of the property. Ptr<ValueInput> propertyValue = pathPatternFeatureInput_var->quantity();  // Set the value of the property, where value_var is a ValueInput. bool returnValue = pathPatternFeatureInput_var->quantity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ValueInput](ValueInput.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |