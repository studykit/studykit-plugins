# DocumentReferences.isValid Property

Parent Object: [DocumentReferences](DocumentReferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentReferences.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentReferences\_var" is a variable referencing a DocumentReferences object. |

"documentReferences\_var" is a variable referencing a DocumentReferences object. ```` ``` #include <Core/Application/DocumentReferences.h>  // Get the value of the property. boolean propertyValue = documentReferences_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |