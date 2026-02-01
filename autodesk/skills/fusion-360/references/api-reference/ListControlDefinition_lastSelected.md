# ListControlDefinition.lastSelected Property

Parent Object: [ListControlDefinition](ListControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListControlDefinition.h>

## Description

Gets the item in the list that was last selected. This can return null in the case where this control is displayed as a list of check boxes and there hasn't been any interaction by the end-user. In the case of a list of check boxes, this returns the item that was last clicked by the user, whether it was to check or uncheck the item. In the case of a list of radio buttons, this always returns the item that is currently selected.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listControlDefinition\_var" is a variable referencing a ListControlDefinition object. |

"listControlDefinition\_var" is a variable referencing a ListControlDefinition object. ```` ``` #include <Core/UserInterface/ListControlDefinition.h>  // Get the value of the property. Ptr<ListItem> propertyValue = listControlDefinition_var->lastSelected(); ``` ```` |

## Property Value

This is a read only property whose value is a [ListItem](ListItem.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |