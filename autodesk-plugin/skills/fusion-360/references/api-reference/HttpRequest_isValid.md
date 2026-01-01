# HttpRequest.isValid Property

Parent Object: [HttpRequest](HttpRequest.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpRequest.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpRequest\_var" is a variable referencing a HttpRequest object. |

"httpRequest\_var" is a variable referencing a HttpRequest object. ```` ``` #include <Core/Application/HttpRequest.h>  // Get the value of the property. boolean propertyValue = httpRequest_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |