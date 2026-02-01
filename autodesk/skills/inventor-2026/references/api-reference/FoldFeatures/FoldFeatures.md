# FoldFeatures Object

## Description

The FoldFeatures collection object provides access to all of the objects in a sheet metal component definition.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../FoldFeatures/FoldFeatures_Add.md) | Method that creates a new fold feature. The newly created CutFeature object is returned. |
| [CreateFoldDefinition](../FoldFeatures/FoldFeatures_CreateFoldDefinition.md) | Method that creates a new FoldDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FoldFeatures/FoldFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../FoldFeatures/FoldFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../FoldFeatures/FoldFeatures_Item.md) | Returns the specified FoldFeature object from the collection. This is the default property of the FoldFeatures collection object. |
| [Type](../FoldFeatures/FoldFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SheetMetalFeatures.FoldFeatures](../SheetMetalFeatures/SheetMetalFeatures_FoldFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |

## Version

Introduced in version 5.3
