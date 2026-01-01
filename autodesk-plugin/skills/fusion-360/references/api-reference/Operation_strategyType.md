# Operation.strategyType Property

Parent Object: [Operation](Operation.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/Operations/Operation.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired. Please use the strategy property instead.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operation\_var" is a variable referencing an Operation object.  ```` ``` # Get the value of the property. propertyValue = operation_var.strategyType ``` ```` |

"operation\_var" is a variable referencing an Operation object. ```` ``` #include <Cam/Operations/Operation.h>  // Get the value of the property. OperationStrategyTypes propertyValue = operation_var->strategyType(); ``` ```` |

## Property Value

This is a read only property whose value is an [OperationStrategyTypes](OperationStrategyTypes.htm).

## Version

Introduced in version January 2016
Retired in version September 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |