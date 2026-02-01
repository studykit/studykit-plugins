# NamedValues.isValid Property

Parent Object: [NamedValues](NamedValues.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedValues.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedValues\_var" is a variable referencing a NamedValues object. |

"namedValues\_var" is a variable referencing a NamedValues object. ```` ``` #include <Core/Application/NamedValues.h>  // Get the value of the property. boolean propertyValue = namedValues_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |