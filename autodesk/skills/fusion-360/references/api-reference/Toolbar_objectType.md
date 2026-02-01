# Toolbar.objectType Property

Parent Object: [Toolbar](Toolbar.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Toolbar.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbar\_var" is a variable referencing a Toolbar object.  ```` ``` # Get the value of the property. propertyValue = toolbar_var.objectType ``` ```` |

"toolbar\_var" is a variable referencing a Toolbar object. ```` ``` #include <Core/UserInterface/Toolbar.h>  // Get the value of the property. string propertyValue = toolbar_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |