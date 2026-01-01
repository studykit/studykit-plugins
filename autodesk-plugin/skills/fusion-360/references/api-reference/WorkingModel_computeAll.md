# WorkingModel.computeAll Method

Parent Object: [WorkingModel](WorkingModel.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/WorkingModel.h>

## Description

Forces a recompute of the entire design. This is the equivalent of the "Compute All" command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workingModel\_var" is a variable referencing a [WorkingModel](WorkingModel.htm) object.```` ``` returnValue = workingModel_var.computeAll() ``` ```` |

"workingModel\_var" is a variable referencing a [WorkingModel](WorkingModel.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the compute completed. This doesn't indicate if all the items in the timeline successfully computed or not. You need to check the health state of each item in the timeline to determine if everything successfully computed or not. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |