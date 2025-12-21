# ModelLeaderNode.InsertNode Method

Parent Object: [ModelLeaderNode](../ModelLeaderNode/ModelLeaderNode.md)

## Description

Method that adds a leader node at the specified position between two existing leader nodes. This is the equivalent of the 'Add Vertex' command in the user interface. This method does not apply for leaf nodes.

## Syntax

ModelLeaderNode.**InsertNode**( ***ChildNode*** As [ModelLeaderNode](../ModelLeaderNode/ModelLeaderNode.md), ***Position*** As [Point](../Point/Point.md) ) As [ModelLeaderNode](../ModelLeaderNode/ModelLeaderNode.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ChildNode | [ModelLeaderNode](../ModelLeaderNode/ModelLeaderNode.md) | LeaderNode object that specifies a child node of this node. The new node will be inserted between these two nodes. If the input node is not an immediate child, an error will occur. |
| Position | [Point](../Point/Point.md) | Point object that specifies the position of the node to add. The method fails if the input position is not on the leader segment connecting the two leader nodes. The point is projected onto the orientation plane. |

## Version

Introduced in version 2018
