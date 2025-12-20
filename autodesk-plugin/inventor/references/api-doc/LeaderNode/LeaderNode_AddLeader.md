# LeaderNode.AddLeader Method

Parent Object: [LeaderNode](../LeaderNode/LeaderNode.md)

## Description

Method that adds a leader branch with the input points. This is the equivalent of the 'Add Leader' command in the user interface.

## Syntax

LeaderNode.**AddLeader**( ***Points*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Points | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | ObjectCollection containing a series of points representing a leader branch, that originates at the node that the branch is being attached to and terminates at the leaf of the branch. If the first point specified has the same position as the node that the branch is being attached to, then the first point is ignored. The last item in the collection can be a GeometryIntent object indicating a geometry to attach the leader branch to. The ObjectCollection must contain at least one item, else the method will fail. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |