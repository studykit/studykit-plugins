# CircularPatternFeature.quantity Property

Parent Object: [CircularPatternFeature](CircularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeature.h>

## Description

Returns the parameter controlling the number of pattern elements, including any suppressed elements. To edit the quantity use properties on the parameter to edit its value. This property returns null in the case where the feature is non-parametric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object. |

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object. ```` ``` #include <Fusion/Features/CircularPatternFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = circularPatternFeature_var->quantity(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |