# Design.analyzeInterference Method

Parent Object: [Design](Design.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/Design.h>

## Description

Calculates the interference between the input bodies and/or occurrences.

## Syntax

* [Python](#Python)
* [C++](#C++)

"design\_var" is a variable referencing a [Design](Design.htm) object.```` ``` returnValue = design_var.analyzeInterference(input) ``` ```` |

"design\_var" is a variable referencing a [Design](Design.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [InterferenceResults](InterferenceResults.htm) | Returns an InterferenceResults object that can be used to examine the interference results. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [InterferenceInput](InterferenceInput.htm) | An InterferenceInput that defines all of the necessary input needed to calculate the interference. An InterferenceInput object is created using the createInterferenceInput method. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Analyze Interference API Sample](AnalyzeInterferenceSample_Sample.htm) | Demonstrates analyzing the interference between components. This uses a direct modeling design because the ability to create bodies that represent the interference volume is only supported in a direct modeling design. |
| [Interference API Sample](InterferenceSample_Sample.htm) | Demonstrates Interference APIs. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |