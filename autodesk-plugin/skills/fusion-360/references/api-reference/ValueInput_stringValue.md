# ValueInput.stringValue Property

Parent Object: [ValueInput](ValueInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ValueInput.h>

## Description

Gets the string value, if there is one. Returns an empty string AND GetLastError returns ValueNotOfType if there is no string value. You can use the valueType property to determine which value type is currently used.

## Syntax

* [Python](#Python)
* [C++](#C++)

"valueInput\_var" is a variable referencing a ValueInput object. |

"valueInput\_var" is a variable referencing a ValueInput object. ```` ``` #include <Core/Application/ValueInput.h>  // Get the value of the property. string propertyValue = valueInput_var->stringValue(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |