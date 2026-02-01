# HttpRequest.url Property

Parent Object: [HttpRequest](HttpRequest.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpRequest.h>

## Description

Gets and sets the URL to make the request to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpRequest\_var" is a variable referencing a HttpRequest object. |

"httpRequest\_var" is a variable referencing a HttpRequest object. ```` ``` #include <Core/Application/HttpRequest.h>  // Get the value of the property. string propertyValue = httpRequest_var->url();  // Set the value of the property, where value_var is a string. bool returnValue = httpRequest_var->url(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |