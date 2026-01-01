# DocumentReference.isValid Property

Parent Object: [DocumentReference](DocumentReference.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentReference.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentReference\_var" is a variable referencing a DocumentReference object. |

"documentReference\_var" is a variable referencing a DocumentReference object. ```` ``` #include <Core/Application/DocumentReference.h>  // Get the value of the property. boolean propertyValue = documentReference_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |