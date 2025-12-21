# GraphicsNodeProxy.AddSurfaceGraphics Method

Parent Object: [GraphicsNodeProxy](../GraphicsNodeProxy/GraphicsNodeProxy.md)

## Description

Method that creates a new SurfaceGraphics object based on the input surface(s).

## Syntax

GraphicsNodeProxy.**AddSurfaceGraphics**( ***Surfaces*** As Object ) As [SurfaceGraphics](../SurfaceGraphics/SurfaceGraphics.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Surfaces | Object | Input object that defines the surfaces. This can be one of the following: SurfaceBody, Face, Faces or a FaceCollection object. If a FaceCollection is provided, all the Face objects in the collection must belong to the same SurfaceBody, else an error will occur. Use the various body primitive creation methods on the TransientBRep object to create bodies for input to this method. |

## Version

Introduced in version 2009
