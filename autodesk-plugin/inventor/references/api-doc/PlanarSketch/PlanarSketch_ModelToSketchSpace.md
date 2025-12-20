# PlanarSketch.ModelToSketchSpace Method

Parent Object: [PlanarSketch](../PlanarSketch/PlanarSketch.md)

## Description

Method that takes a 3D coordinate in model space, projects it onto the sketch plane along the normal of the plane and returns a Point2d object containing the resulting coordinate point in sketch space.

## Syntax

PlanarSketch.**ModelToSketchSpace**( ***ModelCoordinate*** As [Point](../Point/Point.md) ) As [Point2d](../Point2d/Point2d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ModelCoordinate | [Point](../Point/Point.md) | Input Point that specifies the point in model space to be transformed into sketch space. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature - Create Block with Pocket](../../sample-programs/ExtrudeFeature_Sample.md) | This sample demonstrates creating a simple solid consisting a block with a pocket. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |