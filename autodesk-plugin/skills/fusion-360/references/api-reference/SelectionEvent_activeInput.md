# SelectionEvent.activeInput Property

Parent Object: [SelectionEvent](SelectionEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionEvent.h>

## Description

Returns the SelectionCommandInput that is currently active in the command dialog and that the user is selecting entities for. This can be used to determine which set of rules you want to apply to determine if the current entity is selectable or not.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionEvent\_var" is a variable referencing a SelectionEvent object. |

"selectionEvent\_var" is a variable referencing a SelectionEvent object. ```` ``` #include <Core/UserInterface/SelectionEvent.h>  // Get the value of the property. Ptr<SelectionCommandInput> propertyValue = selectionEvent_var->activeInput(); ``` ```` |

## Property Value

This is a read only property whose value is a [SelectionCommandInput](SelectionCommandInput.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |