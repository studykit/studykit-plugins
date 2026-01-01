# SelectionEventArgs.selection Property

Parent Object: [SelectionEventArgs](SelectionEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionEventArgs.h>

## Description

Gets the entity that is valid for selection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionEventArgs\_var" is a variable referencing a SelectionEventArgs object. |

"selectionEventArgs\_var" is a variable referencing a SelectionEventArgs object. ```` ``` #include <Core/UserInterface/SelectionEventArgs.h>  // Get the value of the property. Ptr<Selection> propertyValue = selectionEventArgs_var->selection(); ``` ```` |

## Property Value

This is a read only property whose value is a [Selection](Selection.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |