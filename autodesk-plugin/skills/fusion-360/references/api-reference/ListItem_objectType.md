# ListItem.objectType Property

Parent Object: [ListItem](ListItem.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListItem.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listItem\_var" is a variable referencing a ListItem object.  ```` ``` # Get the value of the property. propertyValue = listItem_var.objectType ``` ```` |

"listItem\_var" is a variable referencing a ListItem object. ```` ``` #include <Core/UserInterface/ListItem.h>  // Get the value of the property. string propertyValue = listItem_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |