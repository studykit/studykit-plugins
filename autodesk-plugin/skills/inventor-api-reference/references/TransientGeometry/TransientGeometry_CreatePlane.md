# TransientGeometry.CreatePlane Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new Plane object. A plane object is infinite. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreatePlane**( ***RootPoint*** As [Point](../Point/Point.md), ***Normal*** As [Vector](../Vector/Vector.md) ) As [Plane](../Plane/Plane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| RootPoint | [Point](../Point/Point.md) | Input Point object that specifies a point on the plane. |
| Normal | [Vector](../Vector/Vector.md) | Input Vector object that specifies the normal direction of the plane. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 4
