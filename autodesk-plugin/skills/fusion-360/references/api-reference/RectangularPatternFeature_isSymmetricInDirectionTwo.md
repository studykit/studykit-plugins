# RectangularPatternFeature.isSymmetricInDirectionTwo Property

Parent Object: [RectangularPatternFeature](RectangularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeature.h>

## Description

Gets and sets if the pattern in direction two is in one direction or symmetric.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = rectangularPatternFeature_var.isSymmetricInDirectionTwo  # Set the value of the property. rectangularPatternFeature_var.isSymmetricInDirectionTwo = propertyValue ``` ```` |

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object. ```` ``` #include <Fusion/Features/RectangularPatternFeature.h>  // Get the value of the property. boolean propertyValue = rectangularPatternFeature_var->isSymmetricInDirectionTwo();  // Set the value of the property, where value_var is a boolean. bool returnValue = rectangularPatternFeature_var->isSymmetricInDirectionTwo(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |