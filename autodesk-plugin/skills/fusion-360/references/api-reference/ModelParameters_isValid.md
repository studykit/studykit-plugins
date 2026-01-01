# ModelParameters.isValid Property

Parent Object: [ModelParameters](ModelParameters.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameters.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameters\_var" is a variable referencing a ModelParameters object. |

"modelParameters\_var" is a variable referencing a ModelParameters object. ```` ``` #include <Fusion/Fusion/ModelParameters.h>  // Get the value of the property. boolean propertyValue = modelParameters_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |