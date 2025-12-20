# RevitExports.Add Method

Parent Object: [RevitExports](../RevitExports/RevitExports.md)

## Description

Method that creates a new Revit model using the information supplied by the input RevitExportDefinition object. If RevitExportDefinition.EnableUpdating is set to True, the new RevitExport is returned and a browser node will for it.

## Syntax

RevitExports.**Add**( ***Definition*** As [RevitExportDefinition](../RevitExportDefinition/RevitExportDefinition.md) ) As [RevitExport](../RevitExport/RevitExport.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [RevitExportDefinition](../RevitExportDefinition/RevitExportDefinition.md) | Input RevitExportDefinition object that defines the RevitExport. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Revit Export sample](../../sample-programs/CreateRevitExportSample_Sample.md) | This sample demonstrates how to create a RevitExport object. |

## Version

Introduced in version 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |