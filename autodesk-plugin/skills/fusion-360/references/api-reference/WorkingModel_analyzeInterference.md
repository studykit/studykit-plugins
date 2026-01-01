# WorkingModel.analyzeInterference Method

Parent Object: [WorkingModel](WorkingModel.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/WorkingModel.h>

## Description

Calculates the interference between the input bodies and/or occurrences.

## Syntax

* [Python](#Python)
* [C++](#C++)

"workingModel\_var" is a variable referencing a [WorkingModel](WorkingModel.htm) object.```` ``` returnValue = workingModel_var.analyzeInterference(input) ``` ```` |

"workingModel\_var" is a variable referencing a [WorkingModel](WorkingModel.htm) object. |

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

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |