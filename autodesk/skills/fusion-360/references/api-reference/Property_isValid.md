# Property.isValid Property

Parent Object: [Property](Property.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Property.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"property\_var" is a variable referencing a Property object. |

"property\_var" is a variable referencing a Property object. ```` ``` #include <Core/Application/Property.h>  // Get the value of the property. boolean propertyValue = property_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |