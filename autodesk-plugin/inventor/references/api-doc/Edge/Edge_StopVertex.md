# Edge.StopVertex Property

Parent Object: [Edge](../Edge/Edge.md)

## Description

Gets the Vertex referenced at the end of this Edge.

## Syntax

Edge.**StopVertex**() As [Vertex](../Vertex/Vertex.md)

## Property Value

This is a read only property whose value is a [Vertex](../Vertex/Vertex.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Edit width extent of an existing flange feature](../../sample-programs/FlangeDefinition_SetEdgeWidthExtent_Sample.md) | This sample demonstrates editing the width extent of an existing flange feature. This expects an existing sheet metal document that contains a flange feature that contains for physical flanges. It changes the type of width extent for each of the physical flanges. The result from the FlangeWidthsCreation sample can be used as the document to run this macro in. |
| [Creating flange features](../../sample-programs/FlangeDefinition_SetOffsetWidthExtent_Sample.md) | Demonstrates creating flange features of various width extents. This creates a new document, creates a face feature and adds a flange feature on four edges. |
| [Finding Bend Extent (Tangent) Edges](../../sample-programs/FlatPattern_GetEdgesOfType_Sample.md) | This sample demonstrates how to retrieve the bend extent edges (a.k.a. tangent edges) associated with the selected bend edge on a flat pattern. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |