# Products Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/Products.h>

## Description

The Products object provides access to all of the products that exist in the document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](Products_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](Products_item.htm) | Function that returns the specified product using an index into the collection. |
| [itemByProductType](Products_itemByProductType.htm) | Returns the specified product, if it exists within this document. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](Products_count.htm) | Returns the number of products within the collection. |
| [isValid](Products_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Products_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Document.products](Document_products.htm), [DrawingDocument.products](DrawingDocument_products.htm), [FusionDocument.products](FusionDocument_products.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Gets all properties using GraphQL](FetchBulkComponentProperties_Sample.htm) | Fetches bulk component properties of the root component and from occurrences via single GraphQL query. |
| [Generate Toolpaths API Sample](GenerateToolpaths_Sample_Sample.htm) | Demonstrates generating the toolpaths in the active document. |
| [Post Toolpaths API Sample](PostToolpaths_Sample_Sample.htm) | Demonstrates posting toolpaths in the active document. |
| [Save and Insert File API Sample](SaveAndInsertSample_Sample.htm) | Demonstrates creating save a new file and then inserting it into a design. To use this sample, have a design open that has been saved and run the script. It will create a new design that contains a cylinder, save it to the same folder the active design was saved to, and then insert it into the active design. |
| [Set part number using GraphQL](SetPartNumberUsingGraphQL_Sample.htm) | Sets part number of root component and from occurrences via GQL query. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |