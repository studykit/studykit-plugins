# InterferenceInput.areCoincidentFacesIncluded Property

Parent Object: [InterferenceInput](InterferenceInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceInput.h>

## Description

Gets and sets whether any coincident faces in the input bodies are considered as interference or not. This property defaults to False for a newly created InterferenceInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"interferenceInput\_var" is a variable referencing an InterferenceInput object. |

"interferenceInput\_var" is a variable referencing an InterferenceInput object. ```` ``` #include <Fusion/Fusion/InterferenceInput.h>  // Get the value of the property. boolean propertyValue = interferenceInput_var->areCoincidentFacesIncluded();  // Set the value of the property, where value_var is a boolean. bool returnValue = interferenceInput_var->areCoincidentFacesIncluded(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Analyze Interference API Sample](AnalyzeInterferenceSample_Sample.htm) | Demonstrates analyzing the interference between components. This uses a direct modeling design because the ability to create bodies that represent the interference volume is only supported in a direct modeling design. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |