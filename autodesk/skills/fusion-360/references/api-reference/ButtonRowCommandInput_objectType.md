# ButtonRowCommandInput.objectType Property

Parent Object: [ButtonRowCommandInput](ButtonRowCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ButtonRowCommandInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"buttonRowCommandInput\_var" is a variable referencing a ButtonRowCommandInput object.  ```` ``` # Get the value of the property. propertyValue = buttonRowCommandInput_var.objectType ``` ```` |

"buttonRowCommandInput\_var" is a variable referencing a ButtonRowCommandInput object. ```` ``` #include <Core/UserInterface/ButtonRowCommandInput.h>  // Get the value of the property. string propertyValue = buttonRowCommandInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |