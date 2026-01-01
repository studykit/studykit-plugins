# HttpRequest.removeHeader Method

Parent Object: [HttpRequest](HttpRequest.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpRequest.h>

## Description

Removes a header from the request.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpRequest\_var" is a variable referencing a [HttpRequest](HttpRequest.htm) object.```` ``` returnValue = httpRequest_var.removeHeader(name) ``` ```` |

"httpRequest\_var" is a variable referencing a [HttpRequest](HttpRequest.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the header was found and removed. |

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