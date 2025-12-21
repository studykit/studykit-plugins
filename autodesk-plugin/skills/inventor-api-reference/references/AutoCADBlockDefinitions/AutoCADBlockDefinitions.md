# AutoCADBlockDefinitions Object

## Description

The AutoCADBlockDefinitions collection object provides access to all the existing AutoCADBlockDefinition objects in a (DWG) drawing document and provides methods to import additional definitions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddFromFile](../AutoCADBlockDefinitions/AutoCADBlockDefinitions_AddFromFile.md) | Method that imports AutoCAD block definitions from an AutoCAD or an Inventor DWG file. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AutoCADBlockDefinitions/AutoCADBlockDefinitions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../AutoCADBlockDefinitions/AutoCADBlockDefinitions_Count.md) | Property that returns the number of items in this collection. |
| [Item](../AutoCADBlockDefinitions/AutoCADBlockDefinitions_Item.md) | Returns the specified AutoCADBlockDefinition object from the collection. |
| [Type](../AutoCADBlockDefinitions/AutoCADBlockDefinitions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingDocument.AutoCADBlockDefinitions](../DrawingDocument/DrawingDocument_AutoCADBlockDefinitions.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [AutoCAD block definitions import](../../sample-programs/AutoCADBlockDefinitions_AddFromFile_Sample.md) | This sample demonstrates importing AutoCAD block definitions from an external dwg file. |
| [AutoCAD block insertion](../../sample-programs/AutoCADBlocks_Add_Sample.md) | Demonstrates inserting an AutoCAD block. |

## Version

Introduced in version 2011
