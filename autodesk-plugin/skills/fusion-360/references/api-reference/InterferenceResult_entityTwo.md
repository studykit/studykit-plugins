# InterferenceResult.entityTwo Property

Parent Object: [InterferenceResult](InterferenceResult.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceResult.h>

## Description

Returns the second entity involved in the interference

## Syntax

* [Python](#Python)
* [C++](#C++)

"interferenceResult\_var" is a variable referencing an InterferenceResult object. |

"interferenceResult\_var" is a variable referencing an InterferenceResult object. ```` ``` #include <Fusion/Fusion/InterferenceResult.h>  // Get the value of the property. Ptr<Base> propertyValue = interferenceResult_var->entityTwo(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

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