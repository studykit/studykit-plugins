# Documents.count Property

Parent Object: [Documents](Documents.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Documents.h>

## Description

Returns the number of currently open documents. This includes documents that are visible and invisible.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documents\_var" is a variable referencing a Documents object. |

"documents\_var" is a variable referencing a Documents object. ```` ``` #include <Core/Application/Documents.h>  // Get the value of the property. uinteger propertyValue = documents_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |