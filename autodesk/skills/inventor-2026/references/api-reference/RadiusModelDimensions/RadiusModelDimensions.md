# RadiusModelDimensions Object

## Description

The RadiusModelDimensions collection object provides access to all of the radial model dimensions in a part or assembly and provides functionality to create new radius dimensions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../RadiusModelDimensions/RadiusModelDimensions_Add.md) | Method that creates an angular dimension. |
| [CreateDefinition](../RadiusModelDimensions/RadiusModelDimensions_CreateDefinition.md) | Method that creates a radius dimension definition. This is a not a radius dimension but an object that encapsulates all of the information that defines a dimension. You use the methods an properties of this object to define the dimension you want to create and then provide it as input to the Add method. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RadiusModelDimensions/RadiusModelDimensions_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../RadiusModelDimensions/RadiusModelDimensions_Count.md) | Property that returns the number of items in this collection. |
| [Item](../RadiusModelDimensions/RadiusModelDimensions_Item.md) | Property that returns an item from the collection. You can provide either the index of the item in the collection, where the first item is index 1, or you can provide the name of the object. |
| [Type](../RadiusModelDimensions/RadiusModelDimensions_Type.md) | Read-only property returning kRadiusModelDimensionsObject indicating this objects type. |

## Accessed From

[ModelDimensions.RadiusModelDimensions](../ModelDimensions/ModelDimensions_RadiusModelDimensions.md)

## Version

Introduced in version 2018
