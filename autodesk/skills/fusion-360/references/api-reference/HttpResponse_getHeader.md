# HttpResponse.getHeader Method

Parent Object: [HttpResponse](HttpResponse.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpResponse.h>

## Description

Gets the value of a header.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpResponse\_var" is a variable referencing a [HttpResponse](HttpResponse.htm) object.```` ``` returnValue = httpResponse_var.getHeader(name) ``` ```` |

"httpResponse\_var" is a variable referencing a [HttpResponse](HttpResponse.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns the value of the header, or empty if the header was not found. You can use the hasHeader method to determine if the header exists before getting it. This is especially useful in the case where the header exists but has an empty string value. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The case insensitive name of the header. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |