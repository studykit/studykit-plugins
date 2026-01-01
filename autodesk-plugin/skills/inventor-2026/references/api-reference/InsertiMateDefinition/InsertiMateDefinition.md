# InsertiMateDefinition Object

Derived from: [iMateDefinition](../iMateDefinition/iMateDefinition.md) Object

## Description

The InsertiMateDefinition object represents an insert iMate definition. It is derived from the iMateDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../InsertiMateDefinition/InsertiMateDefinition_Delete.md) | Method that deletes the iMateDefinition. |
| [GetReferenceKey](../InsertiMateDefinition/InsertiMateDefinition_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../InsertiMateDefinition/InsertiMateDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../InsertiMateDefinition/InsertiMateDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AxesOpposed](../InsertiMateDefinition/InsertiMateDefinition_AxesOpposed.md) | Property that gets whether the direction of the two axes is opposed. |
| [ConstraintLimits](../InsertiMateDefinition/InsertiMateDefinition_ConstraintLimits.md) | Property that returns the ConstraintLimits object that provides access to various limits related settings for the iMate definition. |
| [Distance](../InsertiMateDefinition/InsertiMateDefinition_Distance.md) | Property that returns the Parameter object that controls the distance of the insert iMate definition. |
| [Entity](../InsertiMateDefinition/InsertiMateDefinition_Entity.md) | Property that returns the entity used for the iMate definition. |
| [Exported](../InsertiMateDefinition/InsertiMateDefinition_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [HasReferenceComponent](../InsertiMateDefinition/InsertiMateDefinition_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Identifier](../InsertiMateDefinition/InsertiMateDefinition_Identifier.md) | Property that returns the internal unique identifier for this iMateDefinition. |
| [MatchList](../InsertiMateDefinition/InsertiMateDefinition_MatchList.md) | Gets and sets an array of strings that specifies the priority order for iMate definition matches. |
| [Name](../InsertiMateDefinition/InsertiMateDefinition_Name.md) | Gets the name of this iMateDefinition. |
| [ReferenceComponent](../InsertiMateDefinition/InsertiMateDefinition_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../InsertiMateDefinition/InsertiMateDefinition_ReferencedEntity.md) | Gets the object this entity is dependent on. |
| [SequenceIndex](../InsertiMateDefinition/InsertiMateDefinition_SequenceIndex.md) | Gets the index of this iMateDefinition. |
| [Suppressed](../InsertiMateDefinition/InsertiMateDefinition_Suppressed.md) | Gets the boolean flag that indicates whether this iMateDefinition is suppressed or not. |
| [Type](../InsertiMateDefinition/InsertiMateDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iMateDefinitions.AddInsertiMateDefinition](../iMateDefinitions/iMateDefinitions_AddInsertiMateDefinition.md)

## Derived Classes

[InsertiMateDefinitionProxy](../InsertiMateDefinitionProxy/InsertiMateDefinitionProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add iMate Definition](../../sample-programs/iMateDefinitions_AddMateiMateDefinition_Sample.md) | Add iMate definitions using AddMateiMateDefinition and AddInsertiMateDefinition. |

## Version

Introduced in version 6
