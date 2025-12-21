# MapPointCurve.SetPosition Method

Parent Object: [MapPointCurve](../MapPointCurve/MapPointCurve.md)

## Description

Method that sets the position of the map point. The entity implicitly defines which section the point is for. The position of the map points is defined using a 3D coordinate point. If a map point already exists for the section the input entity is a member of, the current map point will be replaced.

## Syntax

MapPointCurve.**SetPosition**( ***Entity*** As Object, ***Value*** As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | Input entity that is a component of a section. Valid input is a SketchEntity, SketchEntity3D, Edge, WorkPoint or Vertex. |
| Value | Double | Input Double that defines the position of the map point along the input entity as a percentage of the length of the entity. The input value should be between 0 and 1. |

## Version

Introduced in version 6
