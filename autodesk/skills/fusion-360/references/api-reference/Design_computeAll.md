# Design.computeAll Method

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Forces a recompute of the entire design. This is the equivalent of the "Compute All" command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a [Design](Design.htm) object.```` ``` returnValue = design_var.computeAll() ``` ```` |

"design\_var" is a variable referencing a [Design](Design.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the compute completed. This doesn't indicate if all the items in the timeline successfully computed or not. You need to check the health state of each item in the timeline to determine if everything successfully computed or not. |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |