# ComponentList.isValid Property

Parent Object: [ComponentList](ComponentList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/ComponentList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"componentList\_var" is a variable referencing a ComponentList object. |

"componentList\_var" is a variable referencing a ComponentList object. ```` ``` #include <Fusion/Components/ComponentList.h>  // Get the value of the property. boolean propertyValue = componentList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |