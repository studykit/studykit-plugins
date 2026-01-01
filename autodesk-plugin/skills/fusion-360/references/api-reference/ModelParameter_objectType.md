# ModelParameter.objectType Property

Parent Object: [ModelParameter](ModelParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameter.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameter\_var" is a variable referencing a ModelParameter object.  ```` ``` # Get the value of the property. propertyValue = modelParameter_var.objectType ``` ```` |

"modelParameter\_var" is a variable referencing a ModelParameter object. ```` ``` #include <Fusion/Fusion/ModelParameter.h>  // Get the value of the property. string propertyValue = modelParameter_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |