# MarkingMenuEventArgs.isValid Property

Parent Object: [MarkingMenuEventArgs](MarkingMenuEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MarkingMenuEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"markingMenuEventArgs\_var" is a variable referencing a MarkingMenuEventArgs object. |

"markingMenuEventArgs\_var" is a variable referencing a MarkingMenuEventArgs object. ```` ``` #include <Core/UserInterface/MarkingMenuEventArgs.h>  // Get the value of the property. boolean propertyValue = markingMenuEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |