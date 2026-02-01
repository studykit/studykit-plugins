# HttpResponse.isValid Property

Parent Object: [HttpResponse](HttpResponse.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpResponse.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpResponse\_var" is a variable referencing a HttpResponse object. |

"httpResponse\_var" is a variable referencing a HttpResponse object. ```` ``` #include <Core/Application/HttpResponse.h>  // Get the value of the property. boolean propertyValue = httpResponse_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |