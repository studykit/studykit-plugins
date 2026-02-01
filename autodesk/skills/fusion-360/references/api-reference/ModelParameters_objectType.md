# ModelParameters.objectType Property

Parent Object: [ModelParameters](ModelParameters.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameters.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameters\_var" is a variable referencing a ModelParameters object.  ```` ``` # Get the value of the property. propertyValue = modelParameters_var.objectType ``` ```` |

"modelParameters\_var" is a variable referencing a ModelParameters object. ```` ``` #include <Fusion/Fusion/ModelParameters.h>  // Get the value of the property. string propertyValue = modelParameters_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |