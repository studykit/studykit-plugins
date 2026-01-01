# MateiMateDefinition Object

Derived from: [iMateDefinition](../iMateDefinition/iMateDefinition.md) Object

## Description

The MateiMateDefinition object represents a mate iMate definition. It is derived from the iMateDefinition object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MateiMateDefinition/MateiMateDefinition_Delete.md) | Method that deletes the iMateDefinition. |
| [GetReferenceKey](../MateiMateDefinition/MateiMateDefinition_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../MateiMateDefinition/MateiMateDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../MateiMateDefinition/MateiMateDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConstraintLimits](../MateiMateDefinition/MateiMateDefinition_ConstraintLimits.md) | Property that returns the ConstraintLimits object that provides access to various limits related settings for the iMate definition. |
| [Entity](../MateiMateDefinition/MateiMateDefinition_Entity.md) | Property that returns the entity used for the iMate definition. |
| [EntityInferredType](../MateiMateDefinition/MateiMateDefinition_EntityInferredType.md) | Property that returns an enum indicating how the geometry of the entity is interpreted. |
| [Exported](../MateiMateDefinition/MateiMateDefinition_Exported.md) | Read-write property that gets and sets whether the object is exported. Objects must be marked for export in order for them to be derived. |
| [HasReferenceComponent](../MateiMateDefinition/MateiMateDefinition_HasReferenceComponent.md) | Property that specifies if the object was created as the result of a derived part. |
| [Identifier](../MateiMateDefinition/MateiMateDefinition_Identifier.md) | Property that returns the internal unique identifier for this iMateDefinition. |
| [MatchList](../MateiMateDefinition/MateiMateDefinition_MatchList.md) | Gets and sets an array of strings that specifies the priority order for iMate definition matches. |
| [Name](../MateiMateDefinition/MateiMateDefinition_Name.md) | Gets the name of this iMateDefinition. |
| [Offset](../MateiMateDefinition/MateiMateDefinition_Offset.md) | Property that returns the Parameter object that controls the offset of the mate iMate definition. |
| [ReferenceComponent](../MateiMateDefinition/MateiMateDefinition_ReferenceComponent.md) | Property that returns the ReferenceComponent that resulted in the creation of this feature. |
| [ReferencedEntity](../MateiMateDefinition/MateiMateDefinition_ReferencedEntity.md) | Gets the object this entity is dependent on. |
| [SequenceIndex](../MateiMateDefinition/MateiMateDefinition_SequenceIndex.md) | Gets the index of this iMateDefinition. |
| [Suppressed](../MateiMateDefinition/MateiMateDefinition_Suppressed.md) | Gets the boolean flag that indicates whether this iMateDefinition is suppressed or not. |
| [Type](../MateiMateDefinition/MateiMateDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iMateDefinitions.AddMateiMateDefinition](../iMateDefinitions/iMateDefinitions_AddMateiMateDefinition.md)

## Derived Classes

[MateiMateDefinitionProxy](../MateiMateDefinitionProxy/MateiMateDefinitionProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add iMate Definition](../../sample-programs/iMateDefinitions_AddMateiMateDefinition_Sample.md) | Add iMate definitions using AddMateiMateDefinition and AddInsertiMateDefinition. |

## Version

Introduced in version 6
