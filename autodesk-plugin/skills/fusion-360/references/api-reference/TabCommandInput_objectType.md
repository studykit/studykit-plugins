# TabCommandInput.objectType Property

Parent Object: [TabCommandInput](TabCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/TabCommandInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tabCommandInput\_var" is a variable referencing a TabCommandInput object.  ```` ``` # Get the value of the property. propertyValue = tabCommandInput_var.objectType ``` ```` |

"tabCommandInput\_var" is a variable referencing a TabCommandInput object. ```` ``` #include <Core/UserInterface/TabCommandInput.h>  // Get the value of the property. string propertyValue = tabCommandInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |