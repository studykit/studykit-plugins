# Products.isValid Property

Parent Object: [Products](Products.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Products.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"products\_var" is a variable referencing a Products object. |

"products\_var" is a variable referencing a Products object. ```` ``` #include <Core/Application/Products.h>  // Get the value of the property. boolean propertyValue = products_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |