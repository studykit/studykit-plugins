# WorkAxis.SetByNormalToSurface Method

Parent Object: [WorkAxis](../WorkAxis/WorkAxis.md)

## Description

Method that redefines the work axis to pass through the input point and be normal to the input surface.

## Remarks

This method is not valid when the work axis exists in an Assembly component definition.

## Syntax

WorkAxis.**SetByNormalToSurface**( ***Surface*** As Object, ***Point*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Surface | Object | Input object that represents a surface entity. This object can be a Face (planar or non-planar), a WorkPlane or a PlanarSketch object. |
| Point | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, SketchPoint, or SketchPoint3D object. |

## Version

Introduced in version 2008
