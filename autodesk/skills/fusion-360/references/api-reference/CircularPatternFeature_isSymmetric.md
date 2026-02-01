# CircularPatternFeature.isSymmetric Property

Parent Object: [CircularPatternFeature](CircularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeature.h>

## Description

Gets and sets if the angle extent is in one direction or symmetric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = circularPatternFeature_var.isSymmetric  # Set the value of the property. circularPatternFeature_var.isSymmetric = propertyValue ``` ```` |

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object. ```` ``` #include <Fusion/Features/CircularPatternFeature.h>  // Get the value of the property. boolean propertyValue = circularPatternFeature_var->isSymmetric();  // Set the value of the property, where value_var is a boolean. bool returnValue = circularPatternFeature_var->isSymmetric(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |