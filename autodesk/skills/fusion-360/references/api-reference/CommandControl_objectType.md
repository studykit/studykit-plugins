# CommandControl.objectType Property

Parent Object: [CommandControl](CommandControl.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandControl.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandControl\_var" is a variable referencing a CommandControl object.  ```` ``` # Get the value of the property. propertyValue = commandControl_var.objectType ``` ```` |

"commandControl\_var" is a variable referencing a CommandControl object. ```` ``` #include <Core/UserInterface/CommandControl.h>  // Get the value of the property. string propertyValue = commandControl_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |