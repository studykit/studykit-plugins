# BrowserCommandInput.objectType Property

Parent Object: [BrowserCommandInput](BrowserCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/BrowserCommandInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"browserCommandInput\_var" is a variable referencing a BrowserCommandInput object.  ```` ``` # Get the value of the property. propertyValue = browserCommandInput_var.objectType ``` ```` |

"browserCommandInput\_var" is a variable referencing a BrowserCommandInput object. ```` ``` #include <Core/UserInterface/BrowserCommandInput.h>  // Get the value of the property. string propertyValue = browserCommandInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |