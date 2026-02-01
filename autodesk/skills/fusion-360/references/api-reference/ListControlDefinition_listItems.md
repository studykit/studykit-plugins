# ListControlDefinition.listItems Property

Parent Object: [ListControlDefinition](ListControlDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListControlDefinition.h>

## Description

Gets the associated ListControlItems collection through which you can add and modify items in the list.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listControlDefinition\_var" is a variable referencing a ListControlDefinition object. |

"listControlDefinition\_var" is a variable referencing a ListControlDefinition object. ```` ``` #include <Core/UserInterface/ListControlDefinition.h>  // Get the value of the property. Ptr<ListItems> propertyValue = listControlDefinition_var->listItems(); ``` ```` |

## Property Value

This is a read only property whose value is a [ListItems](ListItems.htm).

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |