# SelectionEventArgs.activeInput Property

Parent Object: [SelectionEventArgs](SelectionEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionEventArgs.h>

## Description

Returns the SelectionCommandInput that is currently active in the command dialog and that the user is selecting entities for. This can be used to determine which set of rules you want to apply to determine if the current entity is selectable or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionEventArgs\_var" is a variable referencing a SelectionEventArgs object. |

"selectionEventArgs\_var" is a variable referencing a SelectionEventArgs object. ```` ``` #include <Core/UserInterface/SelectionEventArgs.h>  // Get the value of the property. Ptr<SelectionCommandInput> propertyValue = selectionEventArgs_var->activeInput(); ``` ```` |

## Property Value

This is a read only property whose value is a [SelectionCommandInput](SelectionCommandInput.htm).

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |