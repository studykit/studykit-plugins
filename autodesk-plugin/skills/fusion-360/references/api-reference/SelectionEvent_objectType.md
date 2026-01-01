# SelectionEvent.objectType Property

Parent Object: [SelectionEvent](SelectionEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionEvent.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionEvent\_var" is a variable referencing a SelectionEvent object.  ```` ``` # Get the value of the property. propertyValue = selectionEvent_var.objectType ``` ```` |

"selectionEvent\_var" is a variable referencing a SelectionEvent object. ```` ``` #include <Core/UserInterface/SelectionEvent.h>  // Get the value of the property. string propertyValue = selectionEvent_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |