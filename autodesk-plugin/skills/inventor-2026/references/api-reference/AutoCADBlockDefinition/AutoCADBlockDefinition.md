# AutoCADBlockDefinition Object

## Description

The AutoCADBlockDefinition object represents an AutoCAD block definition.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CopyTo](../AutoCADBlockDefinition/AutoCADBlockDefinition_CopyTo.md) | Method that copies the definition to the target drawing document. |
| [Delete](../AutoCADBlockDefinition/AutoCADBlockDefinition_Delete.md) | Method that deletes the AutoCADBlockDefinition object. This method will fail in the case where the definition is being referenced. This can be determined by using the IsReferenced property. |
| [GetPromptTags](../AutoCADBlockDefinition/AutoCADBlockDefinition_GetPromptTags.md) | Method that returns the tags and their corresponding prompts for field text (attributes) within the block definition. |
| [GetReferenceKey](../AutoCADBlockDefinition/AutoCADBlockDefinition_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AutoCADBlockDefinition/AutoCADBlockDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../AutoCADBlockDefinition/AutoCADBlockDefinition_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [IsReferenced](../AutoCADBlockDefinition/AutoCADBlockDefinition_IsReferenced.md) | Property that specifies if the definition is being referenced or not. A definition is referenced when an instance of the definition has been placed on a sheet. A referenced definition cannot be deleted. |
| [Name](../AutoCADBlockDefinition/AutoCADBlockDefinition_Name.md) | Property that indicates the name of this object or instance. |
| [Parent](../AutoCADBlockDefinition/AutoCADBlockDefinition_Parent.md) | Property returning the parent DrawingDocument object. |
| [Type](../AutoCADBlockDefinition/AutoCADBlockDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AutoCADBlock.Definition](../AutoCADBlock/AutoCADBlock_Definition.md), [AutoCADBlockDefinition.CopyTo](../AutoCADBlockDefinition/AutoCADBlockDefinition_CopyTo.md), [AutoCADBlockDefinitions.Item](../AutoCADBlockDefinitions/AutoCADBlockDefinitions_Item.md), [AutoCADBlockDefinitionsEnumerator.Item](../AutoCADBlockDefinitionsEnumerator/AutoCADBlockDefinitionsEnumerator_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [AutoCAD block insertion](../../sample-programs/AutoCADBlocks_Add_Sample.md) | Demonstrates inserting an AutoCAD block. |

## Version

Introduced in version 2011
