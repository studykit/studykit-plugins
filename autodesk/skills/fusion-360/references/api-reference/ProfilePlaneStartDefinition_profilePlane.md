# ProfilePlaneStartDefinition.profilePlane Property

Parent Object: [ProfilePlaneStartDefinition](ProfilePlaneStartDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ProfilePlaneStartDefinition.h>

## Description

Returns the geometric definition of the profile plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profilePlaneStartDefinition\_var" is a variable referencing a ProfilePlaneStartDefinition object. |

"profilePlaneStartDefinition\_var" is a variable referencing a ProfilePlaneStartDefinition object. ```` ``` #include <Fusion/Features/ProfilePlaneStartDefinition.h>  // Get the value of the property. Ptr<Plane> propertyValue = profilePlaneStartDefinition_var->profilePlane(); ``` ```` |

## Property Value

This is a read only property whose value is a [Plane](Plane.htm).

## Version

Introduced in version November 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |