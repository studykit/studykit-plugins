# CircularPatternFeatureInput.patternComputeOption Property

Parent Object: [CircularPatternFeatureInput](CircularPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeatureInput.h>

## Description

Gets and sets the compute option when patterning features. The default value for this is AdjustPatternCompute. This property only applies when patterning features and is ignored in the direct modeling environment.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeatureInput\_var" is a variable referencing a CircularPatternFeatureInput object. |

"circularPatternFeatureInput\_var" is a variable referencing a CircularPatternFeatureInput object. ```` ``` #include <Fusion/Features/CircularPatternFeatureInput.h>  // Get the value of the property. PatternComputeOptions propertyValue = circularPatternFeatureInput_var->patternComputeOption();  // Set the value of the property, where value_var is a PatternComputeOptions. bool returnValue = circularPatternFeatureInput_var->patternComputeOption(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PatternComputeOptions](PatternComputeOptions.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |