# HttpRequest.create Method

Parent Object: [HttpRequest](HttpRequest.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/HttpRequest.h>

## Description

Creates a new HttpRequest object.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. ```` ```  #include <Core/Application/HttpRequest.h> ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [HttpRequest](HttpRequest.htm) | Returns the new HttpRequest object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| url | string | The URL to make the request to. |
| method | [HttpMethods](HttpMethods.htm) | The method to use for the request. The default is GetMethod.   This is an optional argument whose default value is HttpMethods.GetMethod. |

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