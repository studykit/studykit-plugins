# RectangularPatternFeature.quantityTwo Property

Parent Object: [RectangularPatternFeature](RectangularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeature.h>

## Description

Gets the number of instances in the second direction. Edit the value through ModelParameter. Returns nothing in the case where the feature is non-parametric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object. |

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object. ```` ``` #include <Fusion/Features/RectangularPatternFeature.h>  // Get the value of the property. Ptr<ModelParameter> propertyValue = rectangularPatternFeature_var->quantityTwo(); ``` ```` |

## Property Value

This is a read only property whose value is a [ModelParameter](ModelParameter.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |