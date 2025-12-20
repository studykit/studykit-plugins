# PlanarSketchProxy.ModelToSketchSpace Method

Parent Object: [PlanarSketchProxy](../PlanarSketchProxy/PlanarSketchProxy.md)

## Description

Method that takes a 3D coordinate in model space, projects it onto the sketch plane along the normal of the plane and returns a Point2d object containing the resulting coordinate point in sketch space.

## Syntax

PlanarSketchProxy.**ModelToSketchSpace**( ***ModelCoordinate*** As [Point](../Point/Point.md) ) As [Point2d](../Point2d/Point2d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ModelCoordinate | [Point](../Point/Point.md) | Input Point that specifies the point in model space to be transformed into sketch space. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |