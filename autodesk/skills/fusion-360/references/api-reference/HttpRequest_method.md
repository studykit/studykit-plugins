# HttpRequest.method Property

Parent Object: [HttpRequest](HttpRequest.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpRequest.h>

## Description

Gets and sets the method to use for the request.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpRequest\_var" is a variable referencing a HttpRequest object. |

"httpRequest\_var" is a variable referencing a HttpRequest object. ```` ``` #include <Core/Application/HttpRequest.h>  // Get the value of the property. HttpMethods propertyValue = httpRequest_var->method();  // Set the value of the property, where value_var is a HttpMethods. bool returnValue = httpRequest_var->method(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [HttpMethods](HttpMethods.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |