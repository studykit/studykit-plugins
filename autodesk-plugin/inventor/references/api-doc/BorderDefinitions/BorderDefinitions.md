# BorderDefinitions Object

## Description

The BorderDefinitions collection object provides access to all the existing objects in a drawing document and provides methods to create additional border definitions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../BorderDefinitions/BorderDefinitions_Add.md) | Method that creates a new border definition. The new BorderDefinition object is returned. This method will fail in the case where a sketch is currently active. You can check for this case using the ActiveEditObject property of the Application object to see if a sketch is active. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BorderDefinitions/BorderDefinitions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../BorderDefinitions/BorderDefinitions_Count.md) | Property that returns the number of items in the collection. |
| [Item](../BorderDefinitions/BorderDefinitions_Item.md) | Returns the specified BorderDefinition object from the collection. |
| [Type](../BorderDefinitions/BorderDefinitions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingDocument.BorderDefinitions](../DrawingDocument/DrawingDocument_BorderDefinitions.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Border Create and Insert](../../sample-programs/DrawingDocument_BorderDefinitions_Sample.md) | This sample illustrates creating a new border definition object and using it for a sheet. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |