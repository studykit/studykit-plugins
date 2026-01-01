# SplitFeatures.SplitBody Method

Parent Object: [SplitFeatures](../SplitFeatures/SplitFeatures.md)

## Description

Method that creates a new SplitFeature by splitting a body. The original body is consumed by the operation and two new bodies are created. The new SplitFeature is returned.

## Syntax

SplitFeatures.**SplitBody**( ***SplitTool*** As Object, ***Body*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md) ) As [SplitFeature](../SplitFeature/SplitFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SplitTool | Object | Input Object that specifies the entity that will be used to define the split. The input can be a WorkPlane, WorkSurface, or 2D Path. Use the CreatePath or CreateSpecifiedPath method on the PartFeatures object to create a Path. Currently, a Path may only consist of 2D sketch elements. |
| Body | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody object that specifies the body to be split. |

## Version

Introduced in version 2010
