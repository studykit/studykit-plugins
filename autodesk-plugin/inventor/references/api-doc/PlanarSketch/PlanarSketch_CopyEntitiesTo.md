# PlanarSketch.CopyEntitiesTo Method

Parent Object: [PlanarSketch](../PlanarSketch/PlanarSketch.md)

## Description

Method that copies sketch entities of the sketch to the input target sketch.

## Syntax

PlanarSketch.**CopyEntitiesTo**( ***SketchEntities*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***TargetSketch*** As [Sketch](../Sketch/Sketch.md), [***Position***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchEntities | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object that specifies the sketch entities being copied. |
| TargetSketch | [Sketch](../Sketch/Sketch.md) | Input Sketch object that specifies the target sketch into which the contents of the sketch should be copied. |
| Position | Variant | Optional input Point2d that specifies the position on target sketch to place the copied sketch entities. If not specified the position of the sketch entities in source sketch will be used. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |