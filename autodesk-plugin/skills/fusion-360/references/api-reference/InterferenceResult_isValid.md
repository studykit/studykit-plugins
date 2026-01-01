# InterferenceResult.isValid Property

Parent Object: [InterferenceResult](InterferenceResult.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceResult.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"interferenceResult\_var" is a variable referencing an InterferenceResult object. |

"interferenceResult\_var" is a variable referencing an InterferenceResult object. ```` ``` #include <Fusion/Fusion/InterferenceResult.h>  // Get the value of the property. boolean propertyValue = interferenceResult_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |