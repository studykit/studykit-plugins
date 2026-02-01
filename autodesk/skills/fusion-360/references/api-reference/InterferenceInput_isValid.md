# InterferenceInput.isValid Property

Parent Object: [InterferenceInput](InterferenceInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"interferenceInput\_var" is a variable referencing an InterferenceInput object. |

"interferenceInput\_var" is a variable referencing an InterferenceInput object. ```` ``` #include <Fusion/Fusion/InterferenceInput.h>  // Get the value of the property. boolean propertyValue = interferenceInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |