# MinimumRadiusAnalyses.itemByName Method

Parent Object: [MinimumRadiusAnalyses](MinimumRadiusAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/MinimumRadiusAnalyses.h>

## Description

A method that returns the specified MinimumRadiusAnalysis object using the name of the analysis as displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"minimumRadiusAnalyses\_var" is a variable referencing a [MinimumRadiusAnalyses](MinimumRadiusAnalyses.htm) object.```` ``` returnValue = minimumRadiusAnalyses_var.itemByName(name) ``` ```` |

"minimumRadiusAnalyses\_var" is a variable referencing a [MinimumRadiusAnalyses](MinimumRadiusAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MinimumRadiusAnalysis](MinimumRadiusAnalysis.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the MinimumRadiusAnalysis object as displayed in the browser. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |