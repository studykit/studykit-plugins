# ListItems.isValid Property

Parent Object: [ListItems](ListItems.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ListItems.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"listItems\_var" is a variable referencing a ListItems object. |

"listItems\_var" is a variable referencing a ListItems object. ```` ``` #include <Core/UserInterface/ListItems.h>  // Get the value of the property. boolean propertyValue = listItems_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |