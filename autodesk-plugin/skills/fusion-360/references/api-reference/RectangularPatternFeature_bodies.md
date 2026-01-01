# RectangularPatternFeature.bodies Property

Parent Object: [RectangularPatternFeature](RectangularPatternFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object.  ```` ``` # Get the value of the property. propertyValue = rectangularPatternFeature_var.bodies ``` ```` |

"rectangularPatternFeature\_var" is a variable referencing a RectangularPatternFeature object. ```` ``` #include <Fusion/Features/RectangularPatternFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = rectangularPatternFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |