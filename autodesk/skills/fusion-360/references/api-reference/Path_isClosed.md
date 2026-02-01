# Path.isClosed Property

Parent Object: [Path](Path.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Path.h>

## Description

Indicates if the path is closed or not. Returns True in the case of a closed path.

## Syntax

* [Python](#Python)
* [C++](#C++)

"path\_var" is a variable referencing a Path object. |

"path\_var" is a variable referencing a Path object. ```` ``` #include <Fusion/Features/Path.h>  // Get the value of the property. boolean propertyValue = path_var->isClosed(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |