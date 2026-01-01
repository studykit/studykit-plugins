# HttpResponse.statusCode Property

Parent Object: [HttpResponse](HttpResponse.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpResponse.h>

## Description

Gets the status code of the response.

## Syntax

* [Python](#Python)
* [C++](#C++)

"httpResponse\_var" is a variable referencing a HttpResponse object. |

"httpResponse\_var" is a variable referencing a HttpResponse object. ```` ``` #include <Core/Application/HttpResponse.h>  // Get the value of the property. integer propertyValue = httpResponse_var->statusCode(); ``` ```` |

## Property Value

This is a read only property whose value is an integer.

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