# ModelLeaderNode Object

## Description

The ModelLeaderNode represents the node in the leader of a model leader note.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddLeader](../ModelLeaderNode/ModelLeaderNode_AddLeader.md) | Method that adds a leader branch with the input points. This is the equivalent of the 'Add Leader' command in the user interface. This method will succeed only if the HasRootNode property returns False (i.e. there are no existing leader segments). If there are existing leader segments, you should use the ModelLeaderNode.AddLeader method instead. |
| [Delete](../ModelLeaderNode/ModelLeaderNode_Delete.md) | Method that deletes this leader node, optionally retaining any dependent nodes. |
| [GetReferenceKey](../ModelLeaderNode/ModelLeaderNode_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [InsertNode](../ModelLeaderNode/ModelLeaderNode_InsertNode.md) | Method that adds a leader node at the specified position between two existing leader nodes. This is the equivalent of the 'Add Vertex' command in the user interface. This method does not apply for leaf nodes. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelLeaderNode/ModelLeaderNode_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ModelLeaderNode/ModelLeaderNode_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ChildNodes](../ModelLeaderNode/ModelLeaderNode_ChildNodes.md) | Read-only that returns the child nodes under this node. The count will return 0 if the node is a leaf node. |
| [Intent](../ModelLeaderNode/ModelLeaderNode_Intent.md) | Gets and sets the attached entity of the leaf leader node. |
| [Parent](../ModelLeaderNode/ModelLeaderNode_Parent.md) | Read-only property that returns the parent of the leader. |
| [Position](../ModelLeaderNode/ModelLeaderNode_Position.md) | Gets and sets the leader node location on the sheet. |
| [Type](../ModelLeaderNode/ModelLeaderNode_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ModelLeader.RootNode](../ModelLeader/ModelLeader_RootNode.md), [ModelLeaderNode.InsertNode](../ModelLeaderNode/ModelLeaderNode_InsertNode.md), [ModelLeaderNodesEnumerator.Item](../ModelLeaderNodesEnumerator/ModelLeaderNodesEnumerator_Item.md), [ModelSurfaceTextureSymbolDefinition.RootNode](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_RootNode.md)

## Version

Introduced in version 2018
