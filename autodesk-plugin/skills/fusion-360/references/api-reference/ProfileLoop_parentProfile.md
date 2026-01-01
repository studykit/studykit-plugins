# ProfileLoop.parentProfile Property

Parent Object: [ProfileLoop](ProfileLoop.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileLoop.h>

## Description

Returns the parent Profile object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileLoop\_var" is a variable referencing a ProfileLoop object. |

"profileLoop\_var" is a variable referencing a ProfileLoop object. ```` ``` #include <Fusion/Sketch/ProfileLoop.h>  // Get the value of the property. Ptr<Profile> propertyValue = profileLoop_var->parentProfile(); ``` ```` |

## Property Value

This is a read only property whose value is a [Profile](Profile.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |