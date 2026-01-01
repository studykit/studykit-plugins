# PlanarSketch.AddBySilhouette Method

Parent Object: [PlanarSketch](../PlanarSketch/PlanarSketch.md)

## Description

Method that creates new reference sketch geometry as the silhouette on the input face near the input proximity point.

## Syntax

PlanarSketch.**AddBySilhouette**( ***Face*** As [Face](../Face/Face.md), ***ProximityPoint*** As [Point](../Point/Point.md) ) As [SketchEntity](../SketchEntity/SketchEntity.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Face | [Face](../Face/Face.md) | Input Face that defines a silhouette edge that can be projected onto the sketch plane. |
| ProximityPoint | [Point](../Point/Point.md) | Input that identifies which one of possible multiple results to use. For example, if the input face is a cylinder there are two possible silhouette edges. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |

## Version

Introduced in version 5
