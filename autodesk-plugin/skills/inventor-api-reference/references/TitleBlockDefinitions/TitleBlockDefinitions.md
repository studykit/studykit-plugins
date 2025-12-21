# TitleBlockDefinitions Object

## Description

The TitleBlockDefinitions collection object provides access to all the existing objects in a drawing document and provides methods to create additional title block definitions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../TitleBlockDefinitions/TitleBlockDefinitions_Add.md) | Method that creates a new title block definition. This method will fail in the case where a sketch is currently active. You can check for this case using the ActiveEditObject property of the Application object to see if a sketch is active. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../TitleBlockDefinitions/TitleBlockDefinitions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../TitleBlockDefinitions/TitleBlockDefinitions_Count.md) | Property that returns the number of items in the collection. |
| [Item](../TitleBlockDefinitions/TitleBlockDefinitions_Item.md) | Returns the specified TitleBlockDefinition object from the collection. |
| [Type](../TitleBlockDefinitions/TitleBlockDefinitions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingDocument.TitleBlockDefinitions](../DrawingDocument/DrawingDocument_TitleBlockDefinitions.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |