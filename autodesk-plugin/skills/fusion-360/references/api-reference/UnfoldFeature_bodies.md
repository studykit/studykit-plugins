# UnfoldFeature.bodies Property

Parent Object: [UnfoldFeature](UnfoldFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/UnfoldFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unfoldFeature\_var" is a variable referencing a UnfoldFeature object.  ```` ``` # Get the value of the property. propertyValue = unfoldFeature_var.bodies ``` ```` |

"unfoldFeature\_var" is a variable referencing a UnfoldFeature object. ```` ``` #include <Fusion/SheetMetal/UnfoldFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = unfoldFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |