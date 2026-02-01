# Profile.face Property

Parent Object: [Profile](Profile.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profile.h>

## Description

Returns a temporary BRepFace object that is the same shape as the profile. The geometry of the returned face is defined in the 3D space of the parent sketch of the profile.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profile\_var" is a variable referencing a Profile object.  ```` ``` # Get the value of the property. propertyValue = profile_var.face ``` ```` |

"profile\_var" is a variable referencing a Profile object. ```` ``` #include <Fusion/Sketch/Profile.h>  // Get the value of the property. Ptr<BRepFace> propertyValue = profile_var->face(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepFace](BRepFace.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |