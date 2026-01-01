# SelectionSet.entities Property

Parent Object: [SelectionSet](SelectionSet.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SelectionSet.h>

## Description

Gets and sets the entities in the selection set. Setting this property is the equivalent of using the "Update" option for a selection set in the user-interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionSet\_var" is a variable referencing a SelectionSet object.  ```` ``` # Get the value of the property. propertyValue = selectionSet_var.entities  # Set the value of the property. selectionSet_var.entities = propertyValue ``` ```` |

"selectionSet\_var" is a variable referencing a SelectionSet object. ```` ``` #include <Core/Application/SelectionSet.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = selectionSet_var->entities();  // Set the value of the property, where value_var is a Base. bool returnValue = selectionSet_var->entities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Base](Base.htm).

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |