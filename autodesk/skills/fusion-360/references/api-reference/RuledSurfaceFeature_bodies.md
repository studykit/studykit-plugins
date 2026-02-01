# RuledSurfaceFeature.bodies Property

Parent Object: [RuledSurfaceFeature](RuledSurfaceFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object.  ```` ``` # Get the value of the property. propertyValue = ruledSurfaceFeature_var.bodies ``` ```` |

"ruledSurfaceFeature\_var" is a variable referencing a RuledSurfaceFeature object. ```` ``` #include <Fusion/Features/RuledSurfaceFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = ruledSurfaceFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |