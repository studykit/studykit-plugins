# CircularPatternFeature.axis Property

Parent Object: [CircularPatternFeature](CircularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CircularPatternFeature.h>

## Description

Gets and sets the axis of circular pattern. This can be a sketch line, linear edge, construction axis, an edge/sketch curve that defines an axis (circle, etc.) or a face that defines an axis (cylinder, cone, torus, etc.).

## Syntax

* [Python](#Python)
* [C++](#C++)

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = circularPatternFeature_var.axis  # Set the value of the property. circularPatternFeature_var.axis = propertyValue ``` ```` |

"circularPatternFeature\_var" is a variable referencing a CircularPatternFeature object. ```` ``` #include <Fusion/Features/CircularPatternFeature.h>  // Get the value of the property. Ptr<Base> propertyValue = circularPatternFeature_var->axis();  // Set the value of the property, where value_var is a Base. bool returnValue = circularPatternFeature_var->axis(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |