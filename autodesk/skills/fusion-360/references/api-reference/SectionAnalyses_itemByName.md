# SectionAnalyses.itemByName Method

Parent Object: [SectionAnalyses](SectionAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalyses.h>

## Description

A method that returns the specified SectionAnalysis object using the name of the analysis as displayed in the browser.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalyses\_var" is a variable referencing a [SectionAnalyses](SectionAnalyses.htm) object.```` ``` returnValue = sectionAnalyses_var.itemByName(name) ``` ```` |

"sectionAnalyses\_var" is a variable referencing a [SectionAnalyses](SectionAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SectionAnalysis](SectionAnalysis.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the SectionAnalysis object as displayed in the browser. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |