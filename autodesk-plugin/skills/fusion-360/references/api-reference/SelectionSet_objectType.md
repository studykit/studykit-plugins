# SelectionSet.objectType Property

Parent Object: [SelectionSet](SelectionSet.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SelectionSet.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionSet\_var" is a variable referencing a SelectionSet object.  ```` ``` # Get the value of the property. propertyValue = selectionSet_var.objectType ``` ```` |

"selectionSet\_var" is a variable referencing a SelectionSet object. ```` ``` #include <Core/Application/SelectionSet.h>  // Get the value of the property. string propertyValue = selectionSet_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |