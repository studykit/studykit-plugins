# Properties.isValid Property

Parent Object: [Properties](Properties.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Properties.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"properties\_var" is a variable referencing a Properties object. |

"properties\_var" is a variable referencing a Properties object. ```` ``` #include <Core/Application/Properties.h>  // Get the value of the property. boolean propertyValue = properties_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |