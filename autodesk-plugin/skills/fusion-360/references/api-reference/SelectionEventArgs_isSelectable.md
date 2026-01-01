# SelectionEventArgs.isSelectable Property

Parent Object: [SelectionEventArgs](SelectionEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionEventArgs.h>

## Description

Gets or sets whether this entity should be made available to be selected. The value is initialized to true, so doing nothing will result in the entity being selectable.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionEventArgs\_var" is a variable referencing a SelectionEventArgs object. |

"selectionEventArgs\_var" is a variable referencing a SelectionEventArgs object. ```` ``` #include <Core/UserInterface/SelectionEventArgs.h>  // Get the value of the property. boolean propertyValue = selectionEventArgs_var->isSelectable();  // Set the value of the property, where value_var is a boolean. bool returnValue = selectionEventArgs_var->isSelectable(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |