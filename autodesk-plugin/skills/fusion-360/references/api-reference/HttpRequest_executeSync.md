# HttpRequest.executeSync Method

Parent Object: [HttpRequest](HttpRequest.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpRequest.h>

## Description

Execute this request synchronously. This will block the thread until the request completes.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpRequest\_var" is a variable referencing a [HttpRequest](HttpRequest.htm) object.```` ``` returnValue = httpRequest_var.executeSync() ``` ```` |

"httpRequest\_var" is a variable referencing a [HttpRequest](HttpRequest.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [HttpResponse](HttpResponse.htm) | Returns the response from making this request, or null if an error prevents the request from starting. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Gets all properties using GraphQL](FetchBulkComponentProperties_Sample.htm) | Fetches bulk component properties of the root component and from occurrences via single GraphQL query. |
| [Get part number using GraphQL](FetchPartNumberForComponents_Sample.htm) | Fetches part number of root component and from occurrences via GQL query. |
| [Set part number using GraphQL](SetPartNumberUsingGraphQL_Sample.htm) | Sets part number of root component and from occurrences via GQL query. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |