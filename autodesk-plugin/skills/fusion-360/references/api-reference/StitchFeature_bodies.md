# StitchFeature.bodies Property

Parent Object: [StitchFeature](StitchFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stitchFeature\_var" is a variable referencing a StitchFeature object.  ```` ``` # Get the value of the property. propertyValue = stitchFeature_var.bodies ``` ```` |

"stitchFeature\_var" is a variable referencing a StitchFeature object. ```` ``` #include <Fusion/Features/StitchFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = stitchFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |