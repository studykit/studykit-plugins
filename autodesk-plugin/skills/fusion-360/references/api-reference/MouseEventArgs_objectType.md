# MouseEventArgs.objectType Property

Parent Object: [MouseEventArgs](MouseEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEventArgs.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mouseEventArgs\_var" is a variable referencing a MouseEventArgs object.  ```` ``` # Get the value of the property. propertyValue = mouseEventArgs_var.objectType ``` ```` |

"mouseEventArgs\_var" is a variable referencing a MouseEventArgs object. ```` ``` #include <Core/UserInterface/MouseEventArgs.h>  // Get the value of the property. string propertyValue = mouseEventArgs_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |