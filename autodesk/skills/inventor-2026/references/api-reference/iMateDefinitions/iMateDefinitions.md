# iMateDefinitions Object

## Description

The iMateDefinitions collection provides access to all of the objects in a part or assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddAngleiMateDefinition](../iMateDefinitions/iMateDefinitions_AddAngleiMateDefinition.md) | Method that creates a new angle iMate definition. The newly created AngleiMateDefinition object is returned. |
| [AddCompositeiMateDefinition](../iMateDefinitions/iMateDefinitions_AddCompositeiMateDefinition.md) | Method that creates a new composite iMate definition. The newly created CompositeiMateDefinition object is returned. When iMate definition objects are used as input for a composite iMate, the iMateDefinition objects are no longer directly accessible through the iMateDefinitions collection. They are only accessible through the CompositeiMateDefinition object. |
| [AddFlushiMateDefinition](../iMateDefinitions/iMateDefinitions_AddFlushiMateDefinition.md) | Method that creates a new flush iMate definition. The newly created FlushiMateDefinition object is returned. |
| [AddInsertiMateDefinition](../iMateDefinitions/iMateDefinitions_AddInsertiMateDefinition.md) | Method that creates a new insert iMate definition. The newly created InsertiMateDefinition object is returned. |
| [AddMateiMateDefinition](../iMateDefinitions/iMateDefinitions_AddMateiMateDefinition.md) | Method that creates a new mate iMate definition. |
| [AddRotateRotateiMateDefinition](../iMateDefinitions/iMateDefinitions_AddRotateRotateiMateDefinition.md) | Method that creates a new rotation motion iMate definition. |
| [AddRotateTranslateiMateDefinition](../iMateDefinitions/iMateDefinitions_AddRotateTranslateiMateDefinition.md) | Method that creates a new rotate-translate motion iMate definition. |
| [AddTangentiMateDefinition](../iMateDefinitions/iMateDefinitions_AddTangentiMateDefinition.md) | Method that creates a new tangent iMate definition. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iMateDefinitions/iMateDefinitions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../iMateDefinitions/iMateDefinitions_Count.md) | Property that returns the number of items in this collection. |
| [Item](../iMateDefinitions/iMateDefinitions_Item.md) | Returns the specified iMateDefinition object from the collection. |
| [Type](../iMateDefinitions/iMateDefinitions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.iMateDefinitions](../AssemblyComponentDefinition/AssemblyComponentDefinition_iMateDefinitions.md), [PartComponentDefinition.iMateDefinitions](../PartComponentDefinition/PartComponentDefinition_iMateDefinitions.md), [SheetMetalComponentDefinition.iMateDefinitions](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_iMateDefinitions.md), [WeldmentComponentDefinition.iMateDefinitions](../WeldmentComponentDefinition/WeldmentComponentDefinition_iMateDefinitions.md)

## Version

Introduced in version 6
