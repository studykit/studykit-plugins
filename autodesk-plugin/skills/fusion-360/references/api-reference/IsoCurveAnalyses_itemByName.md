# IsoCurveAnalyses.itemByName Method

Parent Object: [IsoCurveAnalyses](IsoCurveAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/IsoCurveAnalyses.h>

## Description

A method that returns the specified IsoCurveAnalysis object using the name of the analysis as displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"isoCurveAnalyses\_var" is a variable referencing an [IsoCurveAnalyses](IsoCurveAnalyses.htm) object.```` ``` returnValue = isoCurveAnalyses_var.itemByName(name) ``` ```` |

"isoCurveAnalyses\_var" is a variable referencing an [IsoCurveAnalyses](IsoCurveAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [IsoCurveAnalysis](IsoCurveAnalysis.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the IsoCurveAnalysis object as displayed in the browser. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |