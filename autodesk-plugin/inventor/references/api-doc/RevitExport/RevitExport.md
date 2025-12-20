# RevitExport Object

## Description

RevitExport Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RevitExport/RevitExport_Delete.md) | Method that deletes the RevitExport browser node. |
| [GetReferenceKey](../RevitExport/RevitExport_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |
| [Update](../RevitExport/RevitExport_Update.md) | Method that updates the Revit model file that relates with this RevitExport object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RevitExport/RevitExport_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../RevitExport/RevitExport_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [Definition](../RevitExport/RevitExport_Definition.md) | Read-write property that returns the RevitExport definition that defines the current state of the RevitExport. |
| [FullFileName](../RevitExport/RevitExport_FullFileName.md) | Read-only property that returns the full filename of the Revit model file that relates with this RevitExport object. |
| [Name](../RevitExport/RevitExport_Name.md) | Read-only property that gets browser node name of RevitExport.. |
| [Parent](../RevitExport/RevitExport_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../RevitExport/RevitExport_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[RevitExportDefinition.Parent](../RevitExportDefinition/RevitExportDefinition_Parent.md), [RevitExports.Add](../RevitExports/RevitExports_Add.md), [RevitExports.Item](../RevitExports/RevitExports_Item.md)

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