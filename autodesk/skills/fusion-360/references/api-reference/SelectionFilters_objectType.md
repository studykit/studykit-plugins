# SelectionFilters.objectType Property

Parent Object: [SelectionFilters](SelectionFilters.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionFilters.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionFilters\_var" is a variable referencing a SelectionFilters object.  ```` ``` # Get the value of the property. propertyValue = selectionFilters_var.objectType ``` ```` |

"selectionFilters\_var" is a variable referencing a SelectionFilters object. ```` ``` #include <Core/UserInterface/SelectionFilters.h>  // Get the value of the property. string propertyValue = selectionFilters_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |