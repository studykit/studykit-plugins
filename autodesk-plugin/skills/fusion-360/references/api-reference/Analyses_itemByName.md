# Analyses.itemByName Method

Parent Object: [Analyses](Analyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Analyses.h>

## Description

A method that returns the specified Analysis using the name of the analysis as it is displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"analyses\_var" is a variable referencing an [Analyses](Analyses.htm) object.```` ``` returnValue = analyses_var.itemByName(name) ``` ```` |

"analyses\_var" is a variable referencing an [Analyses](Analyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Analysis](Analysis.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the Analysis as it is displayed in the browser. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |