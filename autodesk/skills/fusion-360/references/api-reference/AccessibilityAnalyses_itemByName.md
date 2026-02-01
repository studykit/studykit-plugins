# AccessibilityAnalyses.itemByName Method

Parent Object: [AccessibilityAnalyses](AccessibilityAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/AccessibilityAnalyses.h>

## Description

A method that returns the specified AccessibilityAnalysis object using the name of the analysis as displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"accessibilityAnalyses\_var" is a variable referencing an [AccessibilityAnalyses](AccessibilityAnalyses.htm) object.```` ``` returnValue = accessibilityAnalyses_var.itemByName(name) ``` ```` |

"accessibilityAnalyses\_var" is a variable referencing an [AccessibilityAnalyses](AccessibilityAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [AccessibilityAnalysis](AccessibilityAnalysis.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the AccessibilityAnalysis object as displayed in the browser. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |