# HttpResponse.hasHeader Method

Parent Object: [HttpResponse](HttpResponse.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpResponse.h>

## Description

Gets if the response has a header with the given name. This is useful to distinguish between the case where a header is not set and the case where a header is set to an empty string.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpResponse\_var" is a variable referencing a [HttpResponse](HttpResponse.htm) object.```` ``` returnValue = httpResponse_var.hasHeader(name) ``` ```` |

"httpResponse\_var" is a variable referencing a [HttpResponse](HttpResponse.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | True if a header with this name was set in the response. |

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