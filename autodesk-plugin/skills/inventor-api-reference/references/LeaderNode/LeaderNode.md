# LeaderNode Object

## Description

The LeaderNode object represents a node in a leader.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddLeader](../LeaderNode/LeaderNode_AddLeader.md) | Method that adds a leader branch with the input points. This is the equivalent of the 'Add Leader' command in the user interface. |
| [Delete](../LeaderNode/LeaderNode_Delete.md) | Method that deletes this leader node. |
| [GetReferenceKey](../LeaderNode/LeaderNode_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [InsertNode](../LeaderNode/LeaderNode_InsertNode.md) | Method that adds a LeaderNode at the specified position between two existing leader nodes. This is the equivalent of the 'Add Vertex' command in the user interface. This method does not apply for leaf nodes. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../LeaderNode/LeaderNode_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttachedEntity](../LeaderNode/LeaderNode_AttachedEntity.md) | Gets and sets the attached entity of the leaf leader node. |
| [AttributeSets](../LeaderNode/LeaderNode_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ChildNodes](../LeaderNode/LeaderNode_ChildNodes.md) | Property that returns the children nodes under this node. The count will return 0 if the node is a leaf node. |
| [Parent](../LeaderNode/LeaderNode_Parent.md) | Property that returns the parent of this leader node object. This could either be another LeaderNode object or the Leader object in case of a root node. |
| [Position](../LeaderNode/LeaderNode_Position.md) | Gets and sets the leader node location on the sheet. |
| [Type](../LeaderNode/LeaderNode_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Leader.RootNode](../Leader/Leader_RootNode.md), [LeaderNode.InsertNode](../LeaderNode/LeaderNode_InsertNode.md), [LeaderNodesEnumerator.Item](../LeaderNodesEnumerator/LeaderNodesEnumerator_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add new leader note](../../sample-programs/LeaderNode_Sample.md) | This sample illustrates creating leader text on a sheet. |

## Version

Introduced in version 11
