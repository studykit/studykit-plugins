# Setup.operationType Property

Parent Object: [Setup](Setup.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setup.h>

## Description

Gets the Operation Type. It can be MillingOperation, TurningOperation, JetOperation or AdditiveOperation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setup\_var" is a variable referencing a Setup object. |

"setup\_var" is a variable referencing a Setup object. ```` ``` #include <Cam/CAM/Setup.h>  // Get the value of the property. OperationTypes propertyValue = setup_var->operationType(); ``` ```` |

## Property Value

This is a read only property whose value is an [OperationTypes](OperationTypes.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |