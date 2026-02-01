# CurvatureMapAnalyses.item Method

Parent Object: [CurvatureMapAnalyses](CurvatureMapAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/CurvatureMapAnalyses.h>

## Description

A method that returns the specified CurvatureMapAnalysis object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curvatureMapAnalyses\_var" is a variable referencing a [CurvatureMapAnalyses](CurvatureMapAnalyses.htm) object.```` ``` returnValue = curvatureMapAnalyses_var.item(index) ``` ```` |

"curvatureMapAnalyses\_var" is a variable referencing a [CurvatureMapAnalyses](CurvatureMapAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CurvatureMapAnalysis](CurvatureMapAnalysis.htm) | Returns the specified item or null if an invalid index was specified. |

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