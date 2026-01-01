# HttpResponse.request Property

Parent Object: [HttpResponse](HttpResponse.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpResponse.h>

## Description

Gets the request that generated this response.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpResponse\_var" is a variable referencing a HttpResponse object. |

"httpResponse\_var" is a variable referencing a HttpResponse object. ```` ``` #include <Core/Application/HttpResponse.h>  // Get the value of the property. Ptr<HttpRequest> propertyValue = httpResponse_var->request(); ``` ```` |

## Property Value

This is a read only property whose value is a [HttpRequest](HttpRequest.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |