# LeaderNode.Delete Method

Parent Object: [LeaderNode](../LeaderNode/LeaderNode.md)

## Description

Method that deletes this leader node.

## Remarks

\* If a root node has more than one child node and RetainDependentNodes is true, an error will be returned. \* If a root node has one child node and RetainDependentNodes is true, the root node will be moved to the child node. \* If a root node and RetainDependentNodes is false, all nodes are deleted. \* RetainDependentNodes is ignored for all leaf nodes. \* For leaf nodes where the parent is the root, the leader branch is deleted. \* If leaf node, then new leaf node will be the parent node and the attachment is lost.

## Syntax

LeaderNode.**Delete**( [***RetainDependentNodes***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RetainDependentNodes | Boolean | Optional input Boolean that indicates whether to delete all the dependent nodes as well. If specified to be True, dependent nodes are not deleted. Instead, their ownership is transferred to the parent of this node. If not specified, the argument defaults to False, indicating that all dependent nodes will be deleted. |

## Version

Introduced in version 11
