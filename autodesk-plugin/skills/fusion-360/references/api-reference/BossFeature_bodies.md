# BossFeature.bodies Property

Parent Object: [BossFeature](BossFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bossFeature\_var" is a variable referencing a BossFeature object.  ```` ``` # Get the value of the property. propertyValue = bossFeature_var.bodies ``` ```` |

"bossFeature\_var" is a variable referencing a BossFeature object. ```` ``` #include <Fusion/Plastic/BossFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = bossFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |