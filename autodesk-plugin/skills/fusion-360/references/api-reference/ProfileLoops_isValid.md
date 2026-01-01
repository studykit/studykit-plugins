# ProfileLoops.isValid Property

Parent Object: [ProfileLoops](ProfileLoops.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileLoops.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"profileLoops\_var" is a variable referencing a ProfileLoops object. |

"profileLoops\_var" is a variable referencing a ProfileLoops object. ```` ``` #include <Fusion/Sketch/ProfileLoops.h>  // Get the value of the property. boolean propertyValue = profileLoops_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |