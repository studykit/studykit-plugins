# SketchFixedSpline3D.EditByEdge Method

Parent Object: [SketchFixedSpline3D](../SketchFixedSpline3D/SketchFixedSpline3D.md)

## Description

Method that edits the geometry of a fixed sketch spline based on an input transient Edge.

## Remarks

This method is only valid for SketchFixedSpline3D objects that were created using the AddWithEdge method. The SketchFixedSpline3D object will be updated to reflect the geometry defined by this new Edge. This method will fail if the curve was created using the Add method with a BsplineCurve. This can be determined by checking the IsDefinedByEdge property.

## Syntax

SketchFixedSpline3D.**EditByEdge**( ***TransientEdge*** As [Edge](../Edge/Edge.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TransientEdge | [Edge](../Edge/Edge.md) | Input transient Edge object. |

## Version

Introduced in version 2010
