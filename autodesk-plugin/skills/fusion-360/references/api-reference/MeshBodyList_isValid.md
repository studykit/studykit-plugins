# MeshBodyList.isValid Property

Parent Object: [MeshBodyList](MeshBodyList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/MeshBodyList.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"meshBodyList\_var" is a variable referencing a MeshBodyList object. |

"meshBodyList\_var" is a variable referencing a MeshBodyList object. ```` ``` #include <Fusion/MeshBody/MeshBodyList.h>  // Get the value of the property. boolean propertyValue = meshBodyList_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |