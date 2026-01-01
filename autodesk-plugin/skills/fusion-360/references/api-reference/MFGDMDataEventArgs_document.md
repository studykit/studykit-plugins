# MFGDMDataEventArgs.document Property

Parent Object: [MFGDMDataEventArgs](MFGDMDataEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/MFGDMDataEventArgs.h>

## Description

Provides access to the document that the event is relative to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mFGDMDataEventArgs\_var" is a variable referencing a MFGDMDataEventArgs object. |

"mFGDMDataEventArgs\_var" is a variable referencing a MFGDMDataEventArgs object. ```` ``` #include <Core/Application/MFGDMDataEventArgs.h>  // Get the value of the property. Ptr<Document> propertyValue = mFGDMDataEventArgs_var->document(); ``` ```` |

## Property Value

This is a read only property whose value is a [Document](Document.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Gets all properties using GraphQL](FetchBulkComponentProperties_Sample.htm) | Fetches bulk component properties of the root component and from occurrences via single GraphQL query. |
| [Get part number using GraphQL](FetchPartNumberForComponents_Sample.htm) | Fetches part number of root component and from occurrences via GQL query. |
| [Set part number using GraphQL](SetPartNumberUsingGraphQL_Sample.htm) | Sets part number of root component and from occurrences via GQL query. |

## Version

Introduced in version July 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |