# HttpResponse Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/HttpResponse.h>

## Description

An object that provides the data associated with an HTTP response.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](HttpResponse_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [getHeader](HttpResponse_getHeader.htm) | Gets the value of a header. |
| [hasHeader](HttpResponse_hasHeader.htm) | Gets if the response has a header with the given name. This is useful to distinguish between the case where a header is not set and the case where a header is set to an empty string. |
| [headers](HttpResponse_headers.htm) | Get the response headers. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [data](HttpResponse_data.htm) | Gets the response body data. |
| [isValid](HttpResponse_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](HttpResponse_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [request](HttpResponse_request.htm) | Gets the request that generated this response. |
| [statusCode](HttpResponse_statusCode.htm) | Gets the status code of the response. |

## Accessed From

[HttpEventArgs.response](HttpEventArgs_response.htm), [HttpRequest.executeSync](HttpRequest_executeSync.htm)

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