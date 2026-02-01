# CurvatureCombAnalyses.item Method

Parent Object: [CurvatureCombAnalyses](CurvatureCombAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/CurvatureCombAnalyses.h>

## Description

A method that returns the specified CurvatureCombAnalysis object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curvatureCombAnalyses\_var" is a variable referencing a [CurvatureCombAnalyses](CurvatureCombAnalyses.htm) object.```` ``` returnValue = curvatureCombAnalyses_var.item(index) ``` ```` |

"curvatureCombAnalyses\_var" is a variable referencing a [CurvatureCombAnalyses](CurvatureCombAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CurvatureCombAnalysis](CurvatureCombAnalysis.htm) | Returns the specified item or null if an invalid index was specified. |

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