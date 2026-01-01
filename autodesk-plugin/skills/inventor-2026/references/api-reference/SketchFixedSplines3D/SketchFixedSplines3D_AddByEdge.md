# SketchFixedSplines3D.AddByEdge Method

Parent Object: [SketchFixedSplines3D](../SketchFixedSplines3D/SketchFixedSplines3D.md)

## Description

Method that creates a fixed spline based on an input transient Edge object. This capability is useful because some edges are defined precisely using a procedural algorithm. Converting these to a NURBS curves results in an approximation of the procedural curve. The SketchFixedSpline3D object created with this method has the full accuracy of the procedural curve without any approximation.

## Syntax

SketchFixedSplines3D.**AddByEdge**( ***TransientEdge*** As [Edge](../Edge/Edge.md) ) As [SketchFixedSpline3D](../SketchFixedSpline3D/SketchFixedSpline3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TransientEdge | [Edge](../Edge/Edge.md) | Input Edge object. The edge must be a transient B\-Rep Edge or the method will fail. |

## Version

Introduced in version 2010
