# Profile.boundingBox Property

Parent Object: [Profile](Profile.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profile.h>

## Description

Returns the 3D bounding box of the profile in sketch space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profile\_var" is a variable referencing a Profile object. |

"profile\_var" is a variable referencing a Profile object. ```` ``` #include <Fusion/Sketch/Profile.h>  // Get the value of the property. Ptr<BoundingBox3D> propertyValue = profile_var->boundingBox(); ``` ```` |

## Property Value

This is a read only property whose value is a [BoundingBox3D](BoundingBox3D.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |