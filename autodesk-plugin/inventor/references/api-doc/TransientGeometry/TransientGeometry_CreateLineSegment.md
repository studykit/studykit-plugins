# TransientGeometry.CreateLineSegment Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new LineSegment object. The object created is a transient mathematical object and is not displayed graphically

## Syntax

TransientGeometry.**CreateLineSegment**( ***StartPoint*** As [Point](../Point/Point.md), ***EndPoint*** As [Point](../Point/Point.md) ) As [LineSegment](../LineSegment/LineSegment.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartPoint | [Point](../Point/Point.md) | Input Point object that specifies the start point of the line. |
| EndPoint | [Point](../Point/Point.md) | Input Point object that specifies the end point of the line. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |
| [Transient B-Rep Ruled Surface with Lines](../../sample-programs/TransientBRepRuledSurf1_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses all straight line segments for each of the sections. A part document must be open. |
| [Transient B-Rep Ruled Surface with Arc and Line](../../sample-programs/TransientBRepRuledSurf2_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses straight line segments for once section and an arc for the second. A part document must be open. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |