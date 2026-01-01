# ValueInput.isValid Property

Parent Object: [ValueInput](ValueInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ValueInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"valueInput\_var" is a variable referencing a ValueInput object. |

"valueInput\_var" is a variable referencing a ValueInput object. ```` ``` #include <Core/Application/ValueInput.h>  // Get the value of the property. boolean propertyValue = valueInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |