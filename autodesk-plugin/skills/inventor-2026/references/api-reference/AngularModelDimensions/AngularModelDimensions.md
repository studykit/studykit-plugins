# AngularModelDimensions Object

## Description

The AngularModelDimensions collection object provides access to all of the angular model dimensions in a part or assembly and provides functionality to create new angular dimensions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../AngularModelDimensions/AngularModelDimensions_Add.md) | Method that creates an angular dimension. |
| [CreateDefinition](../AngularModelDimensions/AngularModelDimensions_CreateDefinition.md) | Method that creates an angular dimension definition. This is a not an angular dimension but an object that encapsulates all of the information that defines a dimension. You use the methods an properties of this object to define the dimension you want to create and then provide it as input to the Add method. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AngularModelDimensions/AngularModelDimensions_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../AngularModelDimensions/AngularModelDimensions_Count.md) | Property that returns the number of items in this collection. |
| [Item](../AngularModelDimensions/AngularModelDimensions_Item.md) | Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well. |
| [Type](../AngularModelDimensions/AngularModelDimensions_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[ModelDimensions.AngularModelDimensions](../ModelDimensions/ModelDimensions_AngularModelDimensions.md)

## Version

Introduced in version 2018
