# ModelLeader Object

## Description

The ModelLeader represents the leader of a model leader note.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddLeader](../ModelLeader/ModelLeader_AddLeader.md) | Method that adds a leader branch with the input points. This is the equivalent of the 'Add Leader' command in the user interface. This method will succeed only if the HasRootNode property returns False (i.e. there are no existing leader segments). If there are existing leader segments, you should use the ModelLeaderNode.AddLeader method instead. |
| [GetReferenceKey](../ModelLeader/ModelLeader_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllLeafNodes](../ModelLeader/ModelLeader_AllLeafNodes.md) | Read-only propertythat returns a flat collection of all the leaf nodes in the leader tree. This property will return Nothing if the HasRootNode property returns False. |
| [AllNodes](../ModelLeader/ModelLeader_AllNodes.md) | Read-only that returns a flat collection of all the nodes in the leader tree. This property will return Nothing if the HasRootNode property returns False. |
| [Application](../ModelLeader/ModelLeader_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrowheadType](../ModelLeader/ModelLeader_ArrowheadType.md) | Gets and sets the arrowhead type of the leader. |
| [AttributeSets](../ModelLeader/ModelLeader_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [HasRootNode](../ModelLeader/ModelLeader_HasRootNode.md) | Read-only property that returns if a root node exists for this leader. If False, there are no leader segments associated with this leader and the RootNode property will return Nothing. |
| [Parent](../ModelLeader/ModelLeader_Parent.md) | Read-only property that returns the parent of the leader. |
| [RootNode](../ModelLeader/ModelLeader_RootNode.md) | Read-only property that returns the root node of this leader. This property will return Nothing if the HasRootNode property returns False. |
| [Type](../ModelLeader/ModelLeader_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ModelFeatureControlFrameDefinition.Leader](../ModelFeatureControlFrameDefinition/ModelFeatureControlFrameDefinition_Leader.md), [ModelLeaderNoteDefinition.Leader](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Leader.md), [ModelSurfaceTextureSymbolDefinition.Leader](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Leader.md), [ModelWeldingSymbolDefinitions.Leader](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Leader.md)

## Version

Introduced in version 2018
