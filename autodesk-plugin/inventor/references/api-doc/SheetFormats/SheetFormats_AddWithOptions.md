# SheetFormats.AddWithOptions Method

Parent Object: [SheetFormats](../SheetFormats/SheetFormats.md)

## Description

Creates a new SheetFormat object.

## Syntax

SheetFormats.**AddWithOptions**( ***Sheet*** As [Sheet](../Sheet/Sheet.md), ***Name*** As String, [***Options***] As Variant ) As [SheetFormat](../SheetFormat/SheetFormat.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Sheet | [Sheet](../Sheet/Sheet.md) | Input Sheet object that specifies the sheet to be used as the template for creating the sheet format. |
| Name | String | Input String that defines the name of the sheet format. The name must be unique with respect to all other SheetFormats in the document or an error will occur. |
| Options | Variant | Optional input NameValueMap that specifies more options for creating the sheet format. Valid values are: Name = “FitViewsToSheet”, Value = Boolean value that specifies whether to fit drawing views to sheet or not. If set this to True then the drawing views that are created on this sheet format will be auto-scaled according to the model and the sheet. If set this to False then the drawing views that are created on this sheet format will honor the scale that was saved in the drawing views in the sheet format. If not specified this default to False. |

## Version

Introduced in version 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |