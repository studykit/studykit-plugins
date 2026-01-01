# Selection.entity Property

Parent Object: [Selection](Selection.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Selection.h>

## Description

Gets the selected entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selection\_var" is a variable referencing a Selection object. |

"selection\_var" is a variable referencing a Selection object. ```` ``` #include <Core/UserInterface/Selection.h>  // Get the value of the property. Ptr<Base> propertyValue = selection_var->entity(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |