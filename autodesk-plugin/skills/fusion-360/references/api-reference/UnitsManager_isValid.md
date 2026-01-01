# UnitsManager.isValid Property

Parent Object: [UnitsManager](UnitsManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitsManager.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitsManager\_var" is a variable referencing a UnitsManager object. |

"unitsManager\_var" is a variable referencing a UnitsManager object. ```` ``` #include <Core/Application/UnitsManager.h>  // Get the value of the property. boolean propertyValue = unitsManager_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |