# iMateResults Object

## Description

The iMateResults collection provides access to all of the objects in an assembly. It also supports the methods that allow the creation of iMateResult objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddByiMateAndEntity](../iMateResults/iMateResults_AddByiMateAndEntity.md) | Method that creates a new iMate result. The newly created iMateResult object is returned. If the two inputs do not define a valid iMateResult the method will fail. |
| [AddByTwoiMates](../iMateResults/iMateResults_AddByTwoiMates.md) | Method that creates a new iMate result. The newly created iMateResult object is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iMateResults/iMateResults_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../iMateResults/iMateResults_Count.md) | Property that returns the number of items in the collection. |
| [Item](../iMateResults/iMateResults_Item.md) | Returns the specified iMateResult object from the collection. |
| [Type](../iMateResults/iMateResults_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.iMateResults](../AssemblyComponentDefinition/AssemblyComponentDefinition_iMateResults.md), [WeldmentComponentDefinition.iMateResults](../WeldmentComponentDefinition/WeldmentComponentDefinition_iMateResults.md)

## Version

Introduced in version 6
