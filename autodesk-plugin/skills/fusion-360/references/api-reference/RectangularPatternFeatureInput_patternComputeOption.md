# RectangularPatternFeatureInput.patternComputeOption Property

Parent Object: [RectangularPatternFeatureInput](RectangularPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeatureInput.h>

## Description

Gets and sets the compute option when patterning features. The default value for this is AdjustPatternCompute. This property only applies when patterning features and is ignored in the direct modeling environment.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeatureInput\_var" is a variable referencing a RectangularPatternFeatureInput object. |

"rectangularPatternFeatureInput\_var" is a variable referencing a RectangularPatternFeatureInput object. ```` ``` #include <Fusion/Features/RectangularPatternFeatureInput.h>  // Get the value of the property. PatternComputeOptions propertyValue = rectangularPatternFeatureInput_var->patternComputeOption();  // Set the value of the property, where value_var is a PatternComputeOptions. bool returnValue = rectangularPatternFeatureInput_var->patternComputeOption(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PatternComputeOptions](PatternComputeOptions.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |