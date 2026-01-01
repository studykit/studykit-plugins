# Profile.plane Property

Parent Object: [Profile](Profile.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profile.h>

## Description

Returns the plane the profile is defined in. Profiles are always planar and exist within a single plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profile\_var" is a variable referencing a Profile object. |

"profile\_var" is a variable referencing a Profile object. ```` ``` #include <Fusion/Sketch/Profile.h>  // Get the value of the property. Ptr<Plane> propertyValue = profile_var->plane(); ``` ```` |

## Property Value

This is a read only property whose value is a [Plane](Plane.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |