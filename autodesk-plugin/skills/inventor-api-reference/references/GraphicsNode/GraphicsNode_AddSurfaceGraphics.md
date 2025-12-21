# GraphicsNode.AddSurfaceGraphics Method

Parent Object: [GraphicsNode](../GraphicsNode/GraphicsNode.md)

## Description

Method that creates a new SurfaceGraphics object based on the input surface(s).

## Syntax

GraphicsNode.**AddSurfaceGraphics**( ***Surfaces*** As Object ) As [SurfaceGraphics](../SurfaceGraphics/SurfaceGraphics.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Surfaces | Object | Input object that defines the surfaces. This can be one of the following: SurfaceBody, Face, Faces or a FaceCollection object. If a FaceCollection is provided, all the Face objects in the collection must belong to the same SurfaceBody, else an error will occur. Use the various body primitive creation methods on the TransientBRep object to create bodies for input to this method. |

## Notes

The input body (or the body associated with the input faces) is copied and the copied body is displayed. The client graphics does not remain associative to the original input body and the copied body cannot be edited in any manner.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics from SAT file body](../../sample-programs/GraphicsNode_AddSurfaceGraphics_Sample.md) | The following sample demonstrates how to display client graphics based on bodies read in from a SAT file. |
| [Selection of Surface Graphics Primitives](../../sample-programs/SelectSurfaceGraphicsPrimitives_Sample.md) | This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case). |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Client graphics creation of 3D primitives](../../sample-programs/TransientBRep_CreateSolidCylinderCone_Sample.md) | This sample demonstrates the creation of 3D primitives (cylinder, cone, etc.) using client graphics. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |