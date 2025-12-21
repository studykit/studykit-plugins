# Vertex.Point Property

Parent Object: [Vertex](../Vertex/Vertex.md)

## Description

Property that returns a Point geometry object. The Point object returned provides information about the position of the vertex.

## Syntax

Vertex.**Point**() As [Point](../Point/Point.md)

## Property Value

This is a read only property whose value is a [Point](../Point/Point.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Finding Bend Extent (Tangent) Edges](../../sample-programs/FlatPattern_GetEdgesOfType_Sample.md) | This sample demonstrates how to retrieve the bend extent edges (a.k.a. tangent edges) associated with the selected bend edge on a flat pattern. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |