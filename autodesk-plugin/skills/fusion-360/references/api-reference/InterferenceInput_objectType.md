# InterferenceInput.objectType Property

Parent Object: [InterferenceInput](InterferenceInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/InterferenceInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"interferenceInput\_var" is a variable referencing an InterferenceInput object.  ```` ``` # Get the value of the property. propertyValue = interferenceInput_var.objectType ``` ```` |

"interferenceInput\_var" is a variable referencing an InterferenceInput object. ```` ``` #include <Fusion/Fusion/InterferenceInput.h>  // Get the value of the property. string propertyValue = interferenceInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |