# IsoCurveAnalyses.item Method

Parent Object: [IsoCurveAnalyses](IsoCurveAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/IsoCurveAnalyses.h>

## Description

A method that returns the specified IsoCurveAnalysis object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"isoCurveAnalyses\_var" is a variable referencing an [IsoCurveAnalyses](IsoCurveAnalyses.htm) object.```` ``` returnValue = isoCurveAnalyses_var.item(index) ``` ```` |

"isoCurveAnalyses\_var" is a variable referencing an [IsoCurveAnalyses](IsoCurveAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [IsoCurveAnalysis](IsoCurveAnalysis.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |