# UnfoldMethods Object

## Description

Provides access to the unfold method list (collection of  objects) for a particular sheet metal style.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddBendTableFromFile](../UnfoldMethods/UnfoldMethods_AddBendTableFromFile.md) | Method that adds a BendTable unfold method to the collection and returns the created UnfoldMethod object. |
| [AddEquationUnfoldMethod](../UnfoldMethods/UnfoldMethods_AddEquationUnfoldMethod.md) | Method that adds an equation linear unfold method to the collection and returns the created UnfoldMethod object. The new unfold method will have a single equation that specifies that the bend compensation will be 0 for a bend from 0 to 180 degrees. You can edit the equation to the desired equation using the functionality of the returned UnfoldMethod object. |
| [AddLinearUnfoldMethod](../UnfoldMethods/UnfoldMethods_AddLinearUnfoldMethod.md) | Method that adds a linear unfold method to the collection and returns the created UnfoldMethod object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../UnfoldMethods/UnfoldMethods_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../UnfoldMethods/UnfoldMethods_Count.md) | Property that returns the number of items in the collection. |
| [Item](../UnfoldMethods/UnfoldMethods_Item.md) | Returns the specified UnfoldMethod object from the collection. |
| [Type](../UnfoldMethods/UnfoldMethods_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[SheetMetalComponentDefinition.UnfoldMethods](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_UnfoldMethods.md)

## Version

Introduced in version 5.3
