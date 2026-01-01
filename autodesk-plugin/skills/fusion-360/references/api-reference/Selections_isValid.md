# Selections.isValid Property

Parent Object: [Selections](Selections.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Selections.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selections\_var" is a variable referencing a Selections object. |

"selections\_var" is a variable referencing a Selections object. ```` ``` #include <Core/UserInterface/Selections.h>  // Get the value of the property. boolean propertyValue = selections_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |