# Components.isValid Property

Parent Object: [Components](Components.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Components.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"components\_var" is a variable referencing a Components object. |

"components\_var" is a variable referencing a Components object. ```` ``` #include <Fusion/Components/Components.h>  // Get the value of the property. boolean propertyValue = components_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |