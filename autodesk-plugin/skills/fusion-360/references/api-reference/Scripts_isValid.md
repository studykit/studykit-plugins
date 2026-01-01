# Scripts.isValid Property

Parent Object: [Scripts](Scripts.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Scripts.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"scripts\_var" is a variable referencing a Scripts object. |

"scripts\_var" is a variable referencing a Scripts object. ```` ``` #include <Core/Application/Scripts.h>  // Get the value of the property. boolean propertyValue = scripts_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |