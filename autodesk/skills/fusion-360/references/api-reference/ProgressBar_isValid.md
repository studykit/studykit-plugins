# ProgressBar.isValid Property

Parent Object: [ProgressBar](ProgressBar.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ProgressBar.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"progressBar\_var" is a variable referencing a ProgressBar object. |

"progressBar\_var" is a variable referencing a ProgressBar object. ```` ``` #include <Core/UserInterface/ProgressBar.h>  // Get the value of the property. boolean propertyValue = progressBar_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |