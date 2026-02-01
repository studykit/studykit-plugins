# RectangularPatternFeature.patternComputeOption Property

Parent Object: [RectangularPatternFeature](RectangularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeature.h>

## Description

Gets and sets the compute option for this pattern feature. This property only applies when patterning features and is ignored in the direct modeling environment.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = rectangularPatternFeature_var.patternComputeOption  # Set the value of the property. rectangularPatternFeature_var.patternComputeOption = propertyValue ``` ```` |

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object. ```` ``` #include <Fusion/Features/RectangularPatternFeature.h>  // Get the value of the property. PatternComputeOptions propertyValue = rectangularPatternFeature_var->patternComputeOption();  // Set the value of the property, where value_var is a PatternComputeOptions. bool returnValue = rectangularPatternFeature_var->patternComputeOption(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PatternComputeOptions](PatternComputeOptions.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |