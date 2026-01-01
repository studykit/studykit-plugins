# FlangeFeature.bodies Property

Parent Object: [FlangeFeature](FlangeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlangeFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flangeFeature\_var" is a variable referencing a FlangeFeature object.  ```` ``` # Get the value of the property. propertyValue = flangeFeature_var.bodies ``` ```` |

"flangeFeature\_var" is a variable referencing a FlangeFeature object. ```` ``` #include <Fusion/SheetMetal/FlangeFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = flangeFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |