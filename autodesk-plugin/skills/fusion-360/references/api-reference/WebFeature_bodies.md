# WebFeature.bodies Property

Parent Object: [WebFeature](WebFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/WebFeature.h>

## Description

Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"webFeature\_var" is a variable referencing a WebFeature object.  ```` ``` # Get the value of the property. propertyValue = webFeature_var.bodies ``` ```` |

"webFeature\_var" is a variable referencing a WebFeature object. ```` ``` #include <Fusion/Features/WebFeature.h>  // Get the value of the property. Ptr<BRepBodies> propertyValue = webFeature_var->bodies(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepBodies](BRepBodies.htm).

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |