# SelectionSet.name Property

Parent Object: [SelectionSet](SelectionSet.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SelectionSet.h>

## Description

Gets and sets the name of the SelectionSet object. If a name is assigned that is already used, Fusion will append a counter to the name to make it unique.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionSet\_var" is a variable referencing a SelectionSet object. |

"selectionSet\_var" is a variable referencing a SelectionSet object. ```` ``` #include <Core/Application/SelectionSet.h>  // Get the value of the property. string propertyValue = selectionSet_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = selectionSet_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |