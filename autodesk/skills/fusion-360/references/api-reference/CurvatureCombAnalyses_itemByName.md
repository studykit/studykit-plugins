# CurvatureCombAnalyses.itemByName Method

Parent Object: [CurvatureCombAnalyses](CurvatureCombAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/CurvatureCombAnalyses.h>

## Description

A method that returns the specified CurvatureCombAnalysis object using the name of the analysis as displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curvatureCombAnalyses\_var" is a variable referencing a [CurvatureCombAnalyses](CurvatureCombAnalyses.htm) object.```` ``` returnValue = curvatureCombAnalyses_var.itemByName(name) ``` ```` |

"curvatureCombAnalyses\_var" is a variable referencing a [CurvatureCombAnalyses](CurvatureCombAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CurvatureCombAnalysis](CurvatureCombAnalysis.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the CurvatureCombAnalysis object as displayed in the browser. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |