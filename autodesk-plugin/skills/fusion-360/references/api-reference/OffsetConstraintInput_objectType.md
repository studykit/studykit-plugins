# OffsetConstraintInput.objectType Property

Parent Object: [OffsetConstraintInput](OffsetConstraintInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/OffsetConstraintInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"offsetConstraintInput\_var" is a variable referencing an OffsetConstraintInput object.  ```` ``` # Get the value of the property. propertyValue = offsetConstraintInput_var.objectType ``` ```` |

"offsetConstraintInput\_var" is a variable referencing an OffsetConstraintInput object. ```` ``` #include <Fusion/Sketch/OffsetConstraintInput.h>  // Get the value of the property. string propertyValue = offsetConstraintInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |