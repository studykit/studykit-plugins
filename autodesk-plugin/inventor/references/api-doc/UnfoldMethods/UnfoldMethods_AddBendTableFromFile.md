# UnfoldMethods.AddBendTableFromFile Method

Parent Object: [UnfoldMethods](../UnfoldMethods/UnfoldMethods.md)

## Description

Method that adds a BendTable unfold method to the collection and returns the created UnfoldMethod object.

## Syntax

UnfoldMethods.**AddBendTableFromFile**( ***Name*** As String, ***FileName*** As String ) As [UnfoldMethod](../UnfoldMethod/UnfoldMethod.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String used to specify the name of bendtable UnfoldMethod. This name must be unique with respect to other UnfoldMethod objects. If a unique name is not provided, an error will occur. |
| FileName | String | Input String used to specify the name of the bend table. This is a text file in the format specified in the Sheet Metal documentation. When the UnfoldMethod object is created, the bend table information is extracted from the input file and saved in the sheet metal document. Not relationship is maintained to the original bend table file to it can moved or deleted without any loss of bend table info. This also means that if the text file is changed later, the UnfoldMethod object will not detect the changes and it will have no impact on the bend table. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sheet Metal Style Creation](../../sample-programs/SheetMetalStyles_Sample.md) | This sample illustrates creating a new sheet metal style. It uses a bend table and assumes the sample bend table delivered with Inventor is available. You can edit the path below to reference any existing bend table. To use the sample make sure a bend table is available at the specified path, open a sheet metal document, and run the sample. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |