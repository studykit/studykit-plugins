# SheetMetalComponentDefinition.SetBodySheetMetalStyle2 Method

Parent Object: [SheetMetalComponentDefinition](../SheetMetalComponentDefinition/SheetMetalComponentDefinition.md)

## Description

Method that sets the sheet metal style for a surface body, can ignore computation errors.

## Syntax

SheetMetalComponentDefinition.**SetBodySheetMetalStyle2**( ***Body*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***Value*** As [SheetMetalStyle](../SheetMetalStyle/SheetMetalStyle.md), ***AcceptErors*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Body | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody object that specifies the body to set its sheet metal style. |
| Value | [SheetMetalStyle](../SheetMetalStyle/SheetMetalStyle.md) | Input SheetMetalStyle object that specifies the sheet metal style to set to the body. |
| AcceptErors | Boolean | Optional input Boolean value that indicates if accepts errors when set the sheet metal style to the body. If the AcceptErrors argument is set to True, errors are accepted and the process continues. |

## Version

Introduced in version 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |