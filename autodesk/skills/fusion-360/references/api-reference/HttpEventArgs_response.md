# HttpEventArgs.response Property

Parent Object: [HttpEventArgs](HttpEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpEventArgs.h>

## Description

Returns the response from an http request.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpEventArgs\_var" is a variable referencing a HttpEventArgs object. |

"httpEventArgs\_var" is a variable referencing a HttpEventArgs object. ```` ``` #include <Core/Application/HttpEventArgs.h>  // Get the value of the property. Ptr<HttpResponse> propertyValue = httpEventArgs_var->response(); ``` ```` |

## Property Value

This is a read only property whose value is a [HttpResponse](HttpResponse.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |