# ValueInput.valueType Property

Parent Object: [ValueInput](ValueInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ValueInput.h>

## Description

Returns the type of value this ValueInput currently represents.

## Syntax

* [Python](#Python)
* [C++](#C++)

"valueInput\_var" is a variable referencing a ValueInput object. |

"valueInput\_var" is a variable referencing a ValueInput object. ```` ``` #include <Core/Application/ValueInput.h>  // Get the value of the property. ValueTypes propertyValue = valueInput_var->valueType(); ``` ```` |

## Property Value

This is a read only property whose value is a [ValueTypes](ValueTypes.htm).

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |