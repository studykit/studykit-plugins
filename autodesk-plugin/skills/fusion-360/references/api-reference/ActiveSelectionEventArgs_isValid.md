# ActiveSelectionEventArgs.isValid Property

Parent Object: [ActiveSelectionEventArgs](ActiveSelectionEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ActiveSelectionEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"activeSelectionEventArgs\_var" is a variable referencing an ActiveSelectionEventArgs object. |

"activeSelectionEventArgs\_var" is a variable referencing an ActiveSelectionEventArgs object. ```` ``` #include <Core/UserInterface/ActiveSelectionEventArgs.h>  // Get the value of the property. boolean propertyValue = activeSelectionEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |