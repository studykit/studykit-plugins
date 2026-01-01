# WireEdgeDefinitions.Add Method

Parent Object: [WireEdgeDefinitions](../WireEdgeDefinitions/WireEdgeDefinitions.md)

## Description

Creates a new WireEdgeDefinition within the associated SurfaceBodyDefinition.

## Syntax

WireEdgeDefinitions.**Add**( ***StartVertex*** As [VertexDefinition](../VertexDefinition/VertexDefinition.md), ***EndVertex*** As [VertexDefinition](../VertexDefinition/VertexDefinition.md), ***ModelSpaceCurve*** As Object ) As [WireEdgeDefinition](../WireEdgeDefinition/WireEdgeDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartVertex | [VertexDefinition](../VertexDefinition/VertexDefinition.md) | Input VertexDefinition object that defines the start of the edge. |
| EndVertex | [VertexDefinition](../VertexDefinition/VertexDefinition.md) | Input VertexDefinition object that defines the end of the edge. |
| ModelSpaceCurve | Object | Input transient geometry curve object that defines the shape of this edge using 3d geometry in model space. Valid input is Arc3d, BsplineCurve, Circle, EllipseFull, EllipticalArc, LineSegment and Polyline3D. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |
| [Transient B-Rep Ruled Surface with Lines](../../sample-programs/TransientBRepRuledSurf1_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses all straight line segments for each of the sections. A part document must be open. |
| [Transient B-Rep Ruled Surface with Arc and Line](../../sample-programs/TransientBRepRuledSurf2_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses straight line segments for once section and an arc for the second. A part document must be open. |

## Version

Introduced in version 2013
