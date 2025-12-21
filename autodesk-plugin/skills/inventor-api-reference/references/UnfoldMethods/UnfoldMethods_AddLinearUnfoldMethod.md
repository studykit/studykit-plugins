# UnfoldMethods.AddLinearUnfoldMethod Method

Parent Object: [UnfoldMethods](../UnfoldMethods/UnfoldMethods.md)

## Description

Method that adds a linear unfold method to the collection and returns the created UnfoldMethod object.

## Syntax

UnfoldMethods.**AddLinearUnfoldMethod**( ***Name*** As String, ***Value*** As String ) As [UnfoldMethod](../UnfoldMethod/UnfoldMethod.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String used to specify the name of the UnfoldMethod. This name must be unique with respect to other UnfoldMethod objects. If a unique name is not provided, an error will occur. |
| Value | String | Input String used to specify the k Factor value for this UnfoldMethod object. This can be an expression. This parameter determines where the bend allowance is calculated. The allowable range is from 0 to 1. The bend allowance is calculated using the following equation: 2\*Pi\*(Bend Radius + Linear Offset\*Thickness/2)\*(Bend Angle/360) |

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