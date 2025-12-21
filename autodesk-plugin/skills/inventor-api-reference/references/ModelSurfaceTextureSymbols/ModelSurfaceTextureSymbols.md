# ModelSurfaceTextureSymbols Object

## Description

The ModelSurfaceTextureSymbols collection object provides access to all of the surface texture symbols in a part or assembly and provides functionality to create new surface texture symbols.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ModelSurfaceTextureSymbols/ModelSurfaceTextureSymbols_Add.md) | Method that creates a surface texture symbol. |
| [CreateDefinition](../ModelSurfaceTextureSymbols/ModelSurfaceTextureSymbols_CreateDefinition.md) | Method that creates a surface texture symbol definition. This is a not a surface texture symbol but an object that encapsulates all of the information that defines a surface texture symbol. You use the methods and properties of this object to define the surface texture symbol you want to create and then provide it as input to the Add method. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelSurfaceTextureSymbols/ModelSurfaceTextureSymbols_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../ModelSurfaceTextureSymbols/ModelSurfaceTextureSymbols_Count.md) | Property that returns the number of items in this collection. |
| [Item](../ModelSurfaceTextureSymbols/ModelSurfaceTextureSymbols_Item.md) | Property that returns an item from the collection. You can provide either the index of the item in the collection, where the first item is index 1, or you can provide the name of the object. |
| [Type](../ModelSurfaceTextureSymbols/ModelSurfaceTextureSymbols_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ModelAnnotations.ModelSurfaceTextureSymbols](../ModelAnnotations/ModelAnnotations_ModelSurfaceTextureSymbols.md)

## Version

Introduced in version 2018
