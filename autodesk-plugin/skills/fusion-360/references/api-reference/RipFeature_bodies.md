# RipFeature.bodies Property

Parent Object: [RipFeature](RipFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RipFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ripFeature\_var" is a variable referencing a RipFeature object.  ```` ``` # Get the value of the property. propertyValue = ripFeature_var.bodies ``` ```` |

"ripFeature\_var" is a variable referencing a RipFeature object. ```` ``` #include <Fusion/SheetMetal/RipFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = ripFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |