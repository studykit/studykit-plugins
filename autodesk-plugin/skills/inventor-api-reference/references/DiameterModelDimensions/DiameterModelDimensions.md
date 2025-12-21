# DiameterModelDimensions Object

## Description

The DiameterModelDimensions collection object provides access to all of the diameter model dimensions in a part or assembly and provides functionality to create new diameter dimensions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../DiameterModelDimensions/DiameterModelDimensions_Add.md) | Method that creates a diameter dimension. |
| [CreateDefinition](../DiameterModelDimensions/DiameterModelDimensions_CreateDefinition.md) | Method that creates a diameter dimension definition. This is a not a diameter dimension but an object that encapsulates all of the information that defines a dimension. You use the methods and properties of this object to define the dimension you want to create and then provide it as input to the Add method. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DiameterModelDimensions/DiameterModelDimensions_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../DiameterModelDimensions/DiameterModelDimensions_Count.md) | Property that returns the number of items in this collection. |
| [Item](../DiameterModelDimensions/DiameterModelDimensions_Item.md) | Property that returns an item from the collection. You can provide either the index of the item in the collection, where the first item is index 1, or you can provide the name of the object. |
| [Type](../DiameterModelDimensions/DiameterModelDimensions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ModelDimensions.DiameterModelDimensions](../ModelDimensions/ModelDimensions_DiameterModelDimensions.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |