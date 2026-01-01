# SharedLink.isValid Property

Parent Object: [SharedLink](SharedLink.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/SharedLink.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sharedLink\_var" is a variable referencing a SharedLink object. |

"sharedLink\_var" is a variable referencing a SharedLink object. ```` ``` #include <Core/Dashboard/SharedLink.h>  // Get the value of the property. boolean propertyValue = sharedLink_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |