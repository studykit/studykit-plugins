# DecalInput.isValid Property

Parent Object: [DecalInput](DecalInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/DecalInput.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decalInput\_var" is a variable referencing a DecalInput object. |

"decalInput\_var" is a variable referencing a DecalInput object. ```` ``` #include <Fusion/Image/DecalInput.h>  // Get the value of the property. boolean propertyValue = decalInput_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |