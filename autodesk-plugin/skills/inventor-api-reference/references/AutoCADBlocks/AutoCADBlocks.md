# AutoCADBlocks Object

## Description

The AutoCADBlocks collection object provides access to the instances of the blocks on a specific sheet. It also provides the ability to place blocks onto a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../AutoCADBlocks/AutoCADBlocks_Add.md) | Method that places an AutoCAD block onto the sheet. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AutoCADBlocks/AutoCADBlocks_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../AutoCADBlocks/AutoCADBlocks_Count.md) | Property that returns the number of items in this collection. |
| [Item](../AutoCADBlocks/AutoCADBlocks_Item.md) | Returns the specified AutoCADBlock object from the collection. |
| [Type](../AutoCADBlocks/AutoCADBlocks_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sheet.AutoCADBlocks](../Sheet/Sheet_AutoCADBlocks.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [AutoCAD block insertion](../../sample-programs/AutoCADBlocks_Add_Sample.md) | Demonstrates inserting an AutoCAD block. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |