# LeaderNode.InsertNode Method

Parent Object: [LeaderNode](../LeaderNode/LeaderNode.md)

## Description

Method that adds a LeaderNode at the specified position between two existing leader nodes. This is the equivalent of the 'Add Vertex' command in the user interface. This method does not apply for leaf nodes.

## Syntax

LeaderNode.**InsertNode**( ***ChildNode*** As [LeaderNode](../LeaderNode/LeaderNode.md), ***Position*** As [Point2d](../Point2d/Point2d.md) ) As [LeaderNode](../LeaderNode/LeaderNode.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ChildNode | [LeaderNode](../LeaderNode/LeaderNode.md) | LeaderNode object that specifies a child node of this node. The new node will be inserted between these two nodes. If the input node is not an immediate child, an error will occur. |
| Position | [Point2d](../Point2d/Point2d.md) | Point2d object that specifies the position of the node to add. The method fails if the input position is not on the leader segment connecting the two leader nodes. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add new leader note](../../sample-programs/LeaderNode_Sample.md) | This sample illustrates creating leader text on a sheet. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |