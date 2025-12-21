# PartsLists Object

## Description

The PartsLists collection object provides access to all existing objects on the sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../PartsLists/PartsLists_Add.md) | Method that creates a new PartsList. The newly created PartsList is returned. Currently, this method will fail if the sheet from which this collection was obtained is not active. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PartsLists/PartsLists_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../PartsLists/PartsLists_Count.md) | Property that returns the number of items in this collection. |
| [Item](../PartsLists/PartsLists_Item.md) | Returns the specified PartsList object from the collection. This is the default property of the PartsLists collection object. |
| [Type](../PartsLists/PartsLists_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sheet.PartsLists](../Sheet/Sheet_PartsLists.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Parts List Query](../../sample-programs/PartsLists_Query_Sample.md) | This sample illustrates querying the contents of the parts list. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |