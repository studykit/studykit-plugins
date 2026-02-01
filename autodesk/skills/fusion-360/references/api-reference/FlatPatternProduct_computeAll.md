# FlatPatternProduct.computeAll Method

Parent Object: [FlatPatternProduct](FlatPatternProduct.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternProduct.h>

## Description

Forces a recompute of the entire design. This is the equivalent of the "Compute All" command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternProduct\_var" is a variable referencing a [FlatPatternProduct](FlatPatternProduct.htm) object.```` ``` returnValue = flatPatternProduct_var.computeAll() ``` ```` |

"flatPatternProduct\_var" is a variable referencing a [FlatPatternProduct](FlatPatternProduct.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the compute completed. This doesn't indicate if all the items in the timeline successfully computed or not. You need to check the health state of each item in the timeline to determine if everything successfully computed or not. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |