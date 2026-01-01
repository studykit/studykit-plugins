# CircularPatternFeature.patternComputeOption Property

Parent Object: [CircularPatternFeature](CircularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeature.h>

## Description

Gets and sets the compute option for this pattern feature. This property only applies when patterning features and is ignored in the direct modeling environment.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = circularPatternFeature_var.patternComputeOption  # Set the value of the property. circularPatternFeature_var.patternComputeOption = propertyValue ``` ```` |

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object. ```` ``` #include <Fusion/Features/CircularPatternFeature.h>  // Get the value of the property. PatternComputeOptions propertyValue = circularPatternFeature_var->patternComputeOption();  // Set the value of the property, where value_var is a PatternComputeOptions. bool returnValue = circularPatternFeature_var->patternComputeOption(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PatternComputeOptions](PatternComputeOptions.htm).

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |