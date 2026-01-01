# ProfileLoop.profileCurves Property

Parent Object: [ProfileLoop](ProfileLoop.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileLoop.h>

## Description

Returns a collection of the curves making up this loop.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileLoop\_var" is a variable referencing a ProfileLoop object. |

"profileLoop\_var" is a variable referencing a ProfileLoop object. ```` ``` #include <Fusion/Sketch/ProfileLoop.h>  // Get the value of the property. Ptr<ProfileCurves> propertyValue = profileLoop_var->profileCurves(); ``` ```` |

## Property Value

This is a read only property whose value is a [ProfileCurves](ProfileCurves.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |