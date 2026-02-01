# SelectionEventArgs.additionalEntities Property

Parent Object: [SelectionEventArgs](SelectionEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionEventArgs.h>

## Description

Gets or sets any additional entities that should be pre-highlighted and selected if the entity the mouse is over is selected. If you add an entity that is already selected, it will be unselected. The result of adding additional entities is the same as if they were selected one at a time by the user and the user can unselect each entity one at a time by picking it while it's selected.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionEventArgs\_var" is a variable referencing a SelectionEventArgs object.  ```` ``` # Get the value of the property. propertyValue = selectionEventArgs_var.additionalEntities  # Set the value of the property. selectionEventArgs_var.additionalEntities = propertyValue ``` ```` |

"selectionEventArgs\_var" is a variable referencing a SelectionEventArgs object. ```` ``` #include <Core/UserInterface/SelectionEventArgs.h>  // Get the value of the property. Ptr<ObjectCollection> propertyValue = selectionEventArgs_var->additionalEntities();  // Set the value of the property, where value_var is an ObjectCollection. bool returnValue = selectionEventArgs_var->additionalEntities(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [ObjectCollection](ObjectCollection.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |