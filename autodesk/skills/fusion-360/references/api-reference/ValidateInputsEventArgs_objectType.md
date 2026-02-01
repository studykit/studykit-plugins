# ValidateInputsEventArgs.objectType Property

Parent Object: [ValidateInputsEventArgs](ValidateInputsEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValidateInputsEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"validateInputsEventArgs\_var" is a variable referencing a ValidateInputsEventArgs object.  ```` ``` # Get the value of the property. propertyValue = validateInputsEventArgs_var.objectType ``` ```` |

"validateInputsEventArgs\_var" is a variable referencing a ValidateInputsEventArgs object. ```` ``` #include <Core/UserInterface/ValidateInputsEventArgs.h>  // Get the value of the property. string propertyValue = validateInputsEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |