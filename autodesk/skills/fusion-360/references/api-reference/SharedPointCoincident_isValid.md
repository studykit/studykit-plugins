# SharedPointCoincident.isValid Property

Parent Object: [SharedPointCoincident](SharedPointCoincident.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SharedPointCoincident.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sharedPointCoincident\_var" is a variable referencing a SharedPointCoincident object. |

"sharedPointCoincident\_var" is a variable referencing a SharedPointCoincident object. ```` ``` #include <Fusion/Sketch/SharedPointCoincident.h>  // Get the value of the property. boolean propertyValue = sharedPointCoincident_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version March 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |