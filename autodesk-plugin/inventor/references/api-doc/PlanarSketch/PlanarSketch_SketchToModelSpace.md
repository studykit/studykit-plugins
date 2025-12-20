# PlanarSketch.SketchToModelSpace Method

Parent Object: [PlanarSketch](../PlanarSketch/PlanarSketch.md)

## Description

Method that takes a 2D coordinate in sketch space, and returns a Point3d containing the coordinates of the point in model space.

## Syntax

PlanarSketch.**SketchToModelSpace**( ***SketchCoordinate*** As [Point2d](../Point2d/Point2d.md) ) As [Point](../Point/Point.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchCoordinate | [Point2d](../Point2d/Point2d.md) | Input Point2d that specifies the 2d coordinate in sketch space. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole feature linear placement](../../sample-programs/HoleFeatures_CreateLinearPlacementDefinition_Sample.md) | This sample demonstrates the creation of a hole feature using the linear placement type. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |