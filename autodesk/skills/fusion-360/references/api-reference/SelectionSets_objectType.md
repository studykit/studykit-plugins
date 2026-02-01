# SelectionSets.objectType Property

Parent Object: [SelectionSets](SelectionSets.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SelectionSets.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionSets\_var" is a variable referencing a SelectionSets object.  ```` ``` # Get the value of the property. propertyValue = selectionSets_var.objectType ``` ```` |

"selectionSets\_var" is a variable referencing a SelectionSets object. ```` ``` #include <Core/Application/SelectionSets.h>  // Get the value of the property. string propertyValue = selectionSets_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |