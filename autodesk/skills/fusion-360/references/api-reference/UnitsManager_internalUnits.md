# UnitsManager.internalUnits Property

Parent Object: [UnitsManager](UnitsManager.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/UnitsManager.h>

## Description

Returns a string that represents internal units - i.e. "internalUnits". This can be used when performing conversions via Convert.

## Syntax

* [Python](#Python)
* [C++](#C++)

"unitsManager\_var" is a variable referencing a UnitsManager object. |

"unitsManager\_var" is a variable referencing a UnitsManager object. ```` ``` #include <Core/Application/UnitsManager.h>  // Get the value of the property. string propertyValue = unitsManager_var->internalUnits(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |