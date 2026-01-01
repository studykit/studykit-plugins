# CurvatureMapAnalyses.itemByName Method

Parent Object: [CurvatureMapAnalyses](CurvatureMapAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/CurvatureMapAnalyses.h>

## Description

A method that returns the specified CurvatureMapAnalysis object using the name of the analysis as displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curvatureMapAnalyses\_var" is a variable referencing a [CurvatureMapAnalyses](CurvatureMapAnalyses.htm) object.```` ``` returnValue = curvatureMapAnalyses_var.itemByName(name) ``` ```` |

"curvatureMapAnalyses\_var" is a variable referencing a [CurvatureMapAnalyses](CurvatureMapAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CurvatureMapAnalysis](CurvatureMapAnalysis.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the CurvatureMapAnalysis object as displayed in the browser. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |