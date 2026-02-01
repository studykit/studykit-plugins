# FlatPatternProduct.analyzeInterference Method

Parent Object: [FlatPatternProduct](FlatPatternProduct.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternProduct.h>

## Description

Calculates the interference between the input bodies and/or occurrences.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternProduct\_var" is a variable referencing a [FlatPatternProduct](FlatPatternProduct.htm) object.```` ``` returnValue = flatPatternProduct_var.analyzeInterference(input) ``` ```` |

"flatPatternProduct\_var" is a variable referencing a [FlatPatternProduct](FlatPatternProduct.htm) object. |

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

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |