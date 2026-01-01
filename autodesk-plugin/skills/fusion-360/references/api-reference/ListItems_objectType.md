# ListItems.objectType Property

Parent Object: [ListItems](ListItems.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListItems.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listItems\_var" is a variable referencing a ListItems object.  ```` ``` # Get the value of the property. propertyValue = listItems_var.objectType ``` ```` |

"listItems\_var" is a variable referencing a ListItems object. ```` ``` #include <Core/UserInterface/ListItems.h>  // Get the value of the property. string propertyValue = listItems_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |