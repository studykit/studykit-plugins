# ModelSurfaceTextureSymbolDefinition.AddLeader Method

Parent Object: [ModelSurfaceTextureSymbolDefinition](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition.md)

## Description

Method that adds a leader branch with the input points. This is the equivalent of the 'Add Leader' command in the user interface. This method will succeed only if the HasRootNode property returns False (i.e. there are no existing leader segments). If there are existing leader segments, you should use the ModelLeaderNode.AddLeader method instead.

## Syntax

ModelSurfaceTextureSymbolDefinition.**AddLeader**( ***Points*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Points | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | ObjectCollection containing a series of Point objects representing a leader branch originating at the drawing annotation or symbol. The first point indicates the position of the root node. The last item in the collection can be a GeometryIntent object indicating a geometry to attach the leader branch to. The ObjectCollection must contain at least two items, else the method will fail. The points are projected onto the orientation plane. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |