# DrawingDimensions Object

## Description

The DrawingDimensions object provides access to all of the dimensions ( objects) on the sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Arrange](../DrawingDimensions/DrawingDimensions_Arrange.md) | Method that automatically arranges the input drawing dimensions. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingDimensions/DrawingDimensions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BaselineDimensionSets](../DrawingDimensions/DrawingDimensions_BaselineDimensionSets.md) | Property that returns the BaselineDimensionSets collection object. |
| [ChainDimensionSets](../DrawingDimensions/DrawingDimensions_ChainDimensionSets.md) | Property that returns the ChainDimensionSets collection object. This object provides access to all of the chain dimension sets on the sheet and provides functionality to create new chain dimension sets. |
| [Count](../DrawingDimensions/DrawingDimensions_Count.md) | Property that returns the number of items in the collection. |
| [GeneralDimensions](../DrawingDimensions/DrawingDimensions_GeneralDimensions.md) | Property that returns the GeneralDimensions collection object. This object provides access to all of the general dimensions on the sheet and provides functionality to create new general dimensions. |
| [Item](../DrawingDimensions/DrawingDimensions_Item.md) | Method that returns the specified dimension object from the collection. |
| [OrdinateDimensions](../DrawingDimensions/DrawingDimensions_OrdinateDimensions.md) | Property that returns the OrdinateDimensions collection object. |
| [OrdinateDimensionSets](../DrawingDimensions/DrawingDimensions_OrdinateDimensionSets.md) | Property that returns the OrdinateDimensionSets collection object. |
| [Type](../DrawingDimensions/DrawingDimensions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sheet.DrawingDimensions](../Sheet/Sheet_DrawingDimensions.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Baseline dimension sets](../../sample-programs/BaselineDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a baseline set dimension in a drawing. |
| [Dimensions - edit](../../sample-programs/DrawingDimension_Sample.md) | This sample demonstrates the editing of sheet dimensions and the associated dimension style. |

## Version

Introduced in version 9
