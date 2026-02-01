# OperationStrategy.isTurningStrategy Property![](../images/TestTubeLarge.png)

Parent Object: [OperationStrategy](OperationStrategy.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationStrategy.h>

## Description

Gets whether given OperationStrategy is a turning strategy.

## Syntax

* [Python](#Python)
* [C++](#C++)

"operationStrategy\_var" is a variable referencing an OperationStrategy object. |

"operationStrategy\_var" is a variable referencing an OperationStrategy object. ```` ``` #include <Cam/Operations/OperationStrategy.h>  // Get the value of the property. boolean propertyValue = operationStrategy_var->isTurningStrategy(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |