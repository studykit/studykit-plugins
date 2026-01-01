# MouseEvent.objectType Property

Parent Object: [MouseEvent](MouseEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mouseEvent\_var" is a variable referencing a MouseEvent object.  ```` ``` # Get the value of the property. propertyValue = mouseEvent_var.objectType ``` ```` |

"mouseEvent\_var" is a variable referencing a MouseEvent object. ```` ``` #include <Core/UserInterface/MouseEvent.h>  // Get the value of the property. string propertyValue = mouseEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |