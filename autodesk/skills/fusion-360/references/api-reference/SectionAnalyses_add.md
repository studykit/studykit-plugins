# SectionAnalyses.add Method

Parent Object: [SectionAnalyses](SectionAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalyses.h>

## Description

Creates a new Section Analysis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalyses\_var" is a variable referencing a [SectionAnalyses](SectionAnalyses.htm) object.```` ``` returnValue = sectionAnalyses_var.add(input) ``` ```` |

"sectionAnalyses\_var" is a variable referencing a [SectionAnalyses](SectionAnalyses.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SectionAnalysis](SectionAnalysis.htm) | Returns the new SectionAnalysis object if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [SectionAnalysisInput](SectionAnalysisInput.htm) | A SectionAnalysisInput object that defines how the section analysis should be created. Use the createInput method to create a new SectionAnalysisInput object. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |