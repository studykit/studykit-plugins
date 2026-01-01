# DocumentEvent.isValid Property

Parent Object: [DocumentEvent](DocumentEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEvent.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentEvent\_var" is a variable referencing a DocumentEvent object. |

"documentEvent\_var" is a variable referencing a DocumentEvent object. ```` ``` #include <Core/Application/DocumentEvent.h>  // Get the value of the property. boolean propertyValue = documentEvent_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |