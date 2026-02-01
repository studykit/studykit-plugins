# ActiveSelectionEventArgs.currentSelection Property

Parent Object: [ActiveSelectionEventArgs](ActiveSelectionEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ActiveSelectionEventArgs.h>

## Description

The list of all of the current selections. This is the same set of selections accessed through the UserInterface.activeSelection object. An empty array can be returned in the case where the selection has been cleared which can occur by the user unselecting and entity, terminating the select command pressing Escape or running another command or clicking the mouse in an open area of the canvas.

## Syntax

* [Python](#Python)
* [C++](#C++)

"activeSelectionEventArgs\_var" is a variable referencing an ActiveSelectionEventArgs object. |

"activeSelectionEventArgs\_var" is a variable referencing an ActiveSelectionEventArgs object. ```` ``` #include <Core/UserInterface/ActiveSelectionEventArgs.h>  // Get the value of the property. std::vector<Ptr<Selection>> propertyValue = activeSelectionEventArgs_var->currentSelection(); ``` ```` |

## Property Value

This is a read only property whose value is an array of type [Selection](Selection.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |