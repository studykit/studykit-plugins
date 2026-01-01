# Selection.isValid Property

Parent Object: [Selection](Selection.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Selection.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selection\_var" is a variable referencing a Selection object. |

"selection\_var" is a variable referencing a Selection object. ```` ``` #include <Core/UserInterface/Selection.h>  // Get the value of the property. boolean propertyValue = selection_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |