# PathPatternFeatureInput.isOrientationAlongPath Property

Parent Object: [PathPatternFeatureInput](PathPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeatureInput.h>

## Description

Gets and sets if the orientation is along path. If false, the orientation is identical.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeatureInput\_var" is a variable referencing a PathPatternFeatureInput object. |

"pathPatternFeatureInput\_var" is a variable referencing a PathPatternFeatureInput object. ```` ``` #include <Fusion/Features/PathPatternFeatureInput.h>  // Get the value of the property. boolean propertyValue = pathPatternFeatureInput_var->isOrientationAlongPath();  // Set the value of the property, where value_var is a boolean. bool returnValue = pathPatternFeatureInput_var->isOrientationAlongPath(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |