# MapPointCurve.GetPosition Method

Parent Object: [MapPointCurve](../MapPointCurve/MapPointCurve.md)

## Description

Method that gets the position of the specified map point along the input entity.

## Syntax

MapPointCurve.**GetPosition**( ***Index*** As Long, ***Entity*** As Object, ***Result*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Long | Input Long that defines which map point to get the position for. The first map point has an index of 1. |
| Entity | Object | Output entity that is the component of the section that was used to define the position of the map point. This argument can be a SketchEntity, SketchEntity3D, Edge, WorkPoint or Vertex. |
| Result | Double |  |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |