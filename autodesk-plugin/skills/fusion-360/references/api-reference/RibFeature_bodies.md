# RibFeature.bodies Property

Parent Object: [RibFeature](RibFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RibFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ribFeature\_var" is a variable referencing a RibFeature object.  ```` ``` # Get the value of the property. propertyValue = ribFeature_var.bodies ``` ```` |

"ribFeature\_var" is a variable referencing a RibFeature object. ```` ``` #include <Fusion/Features/RibFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = ribFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |