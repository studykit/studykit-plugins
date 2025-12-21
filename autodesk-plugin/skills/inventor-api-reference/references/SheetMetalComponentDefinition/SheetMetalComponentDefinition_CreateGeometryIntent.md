# SheetMetalComponentDefinition.CreateGeometryIntent Method

Parent Object: [SheetMetalComponentDefinition](../SheetMetalComponentDefinition/SheetMetalComponentDefinition.md)

## Description

Method that creates a GeometryIntent object. GeometryIntent objects are used as input when creating annotations in the model. They are used to identify geometry and optionally specific locations on that geometry.

## Syntax

SheetMetalComponentDefinition.**CreateGeometryIntent**( ***Geometry*** As Object, [***Intent***] As Variant ) As [GeometryIntent](../GeometryIntent/GeometryIntent.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Geometry | Object | Input object that specifies the geometry. Valid input objects are Vertex, WorkPoint, SketchPoint, SketchPoint3d, WorkAxis, SketchLine, SketchLine3d, SketchCircle, SketchCircle3d, Edge, or Face objects. |
| Intent | Variant | Optional input that specifies a specific position on the geometry. This can be a value from PointIntentEnum, an entity if the intent is the intersection of two geometries, a Point object that specifies a position on the geometry relative to model space, a double value indicating a position in the parametric space of the input curve, and a Point2d object that specifies a point in the parametric space of a surface. |

## Version

Introduced in version 2018
