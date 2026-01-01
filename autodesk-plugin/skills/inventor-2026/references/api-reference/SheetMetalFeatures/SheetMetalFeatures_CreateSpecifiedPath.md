# SheetMetalFeatures.CreateSpecifiedPath Method

Parent Object: [SheetMetalFeatures](../SheetMetalFeatures/SheetMetalFeatures.md)

## Description

Method that creates a path used to define the shape of several part features such as sweep, rectangular pattern, split, etc. The new path is returned. This method will fail if the input curves are not connected end-to-end.

## Syntax

SheetMetalFeatures.**CreateSpecifiedPath**( ***SketchCurves*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md) ) As [Path](../Path/Path.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SketchCurves | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input (planar or 3D) sketch entities. These are entities that are part of the desired path. The input curves must form a contiguous set. |

## Version

Introduced in version 8
