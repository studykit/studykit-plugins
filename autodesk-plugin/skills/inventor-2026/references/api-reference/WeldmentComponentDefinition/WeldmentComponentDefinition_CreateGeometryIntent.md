# WeldmentComponentDefinition.CreateGeometryIntent Method

Parent Object: [WeldmentComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition.md)

## Description

Method that creates a GeometryIntent object. GeometryIntent objects are used as input when creating assembly joints. They are used to identify geometry and specific locations on that geometry.

## Syntax

WeldmentComponentDefinition.**CreateGeometryIntent**( ***Geometry*** As Object, [***Intent***] As Variant ) As [GeometryIntent](../GeometryIntent/GeometryIntent.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Geometry | Object | Input object that specifies the geometry.  Valid input objects are proxies of SketchLine, SketchCircle, SketchArc, SketchEllipse, SketchEllipticalArc, Edge, or Face objects. |
| Intent | Variant | Optional input that specifies a specific position on the geometry. This can be a value from PointIntentEnum, a Point, or a GeometryIntent object that specifies a position on the geometry relative to model space, a double value indicating a position in the parametric space of the input curve. |

## Version

Introduced in version 2014
