# InterferenceResult.objectType Property

Parent Object: [InterferenceResult](InterferenceResult.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceResult.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"interferenceResult\_var" is a variable referencing an InterferenceResult object.  ```` ``` # Get the value of the property. propertyValue = interferenceResult_var.objectType ``` ```` |

"interferenceResult\_var" is a variable referencing an InterferenceResult object. ```` ``` #include <Fusion/Fusion/InterferenceResult.h>  // Get the value of the property. string propertyValue = interferenceResult_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |