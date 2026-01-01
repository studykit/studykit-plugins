# Toolbars.objectType Property

Parent Object: [Toolbars](Toolbars.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Toolbars.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"toolbars\_var" is a variable referencing a Toolbars object.  ```` ``` # Get the value of the property. propertyValue = toolbars_var.objectType ``` ```` |

"toolbars\_var" is a variable referencing a Toolbars object. ```` ``` #include <Core/UserInterface/Toolbars.h>  // Get the value of the property. string propertyValue = toolbars_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |