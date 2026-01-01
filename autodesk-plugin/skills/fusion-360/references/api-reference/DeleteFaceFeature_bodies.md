# DeleteFaceFeature.bodies Property

Parent Object: [DeleteFaceFeature](DeleteFaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DeleteFaceFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"deleteFaceFeature\_var" is a variable referencing a DeleteFaceFeature object.  ```` ``` # Get the value of the property. propertyValue = deleteFaceFeature_var.bodies ``` ```` |

"deleteFaceFeature\_var" is a variable referencing a DeleteFaceFeature object. ```` ``` #include <Fusion/Features/DeleteFaceFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = deleteFaceFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |