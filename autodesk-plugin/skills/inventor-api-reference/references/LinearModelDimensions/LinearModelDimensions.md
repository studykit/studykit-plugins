# LinearModelDimensions Object

## Description

The LinearModelDimensions collection object provides access to all of the linear model dimensions in a part or assembly and provides functionality to create new linear dimensions.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../LinearModelDimensions/LinearModelDimensions_Add.md) | Method that creates a linear dimension. |
| [CreateDefinition](../LinearModelDimensions/LinearModelDimensions_CreateDefinition.md) | Method that creates a linear dimension definition. This is a not a linear dimension but an object that encapsulates all of the information that defines a dimension. You use the methods an properties of this object to define the dimension you want to create and then provide it as input to the Add method. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../LinearModelDimensions/LinearModelDimensions_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../LinearModelDimensions/LinearModelDimensions_Count.md) | Property that returns the number of items in this collection. |
| [Item](../LinearModelDimensions/LinearModelDimensions_Item.md) | Property that returns an item from the collection. You can provide either the index of the item in the collection, where the first item is index 1, or you can provide the name of the object. |
| [Type](../LinearModelDimensions/LinearModelDimensions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ModelDimensions.LinearModelDimensions](../ModelDimensions/ModelDimensions_LinearModelDimensions.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |