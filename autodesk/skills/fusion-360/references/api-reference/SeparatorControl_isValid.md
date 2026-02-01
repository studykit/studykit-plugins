# SeparatorControl.isValid Property

Parent Object: [SeparatorControl](SeparatorControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SeparatorControl.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"separatorControl\_var" is a variable referencing a SeparatorControl object. |

"separatorControl\_var" is a variable referencing a SeparatorControl object. ```` ``` #include <Core/UserInterface/SeparatorControl.h>  // Get the value of the property. boolean propertyValue = separatorControl_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |