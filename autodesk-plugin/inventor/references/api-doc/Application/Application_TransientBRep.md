# Application.TransientBRep Property

Parent Object: [Application](../Application/Application.md)

## Description

Property that returns the TransientBRep object.

## Syntax

Application.**TransientBRep**() As [TransientBRep](../TransientBRep/TransientBRep.md)

## Property Value

This is a read only property whose value is a [TransientBRep](../TransientBRep/TransientBRep.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics from SAT file body](../../sample-programs/GraphicsNode_AddSurfaceGraphics_Sample.md) | The following sample demonstrates how to display client graphics based on bodies read in from a SAT file. |
| [3D Curve from Parametric Curve](../../sample-programs/ParameterCurveTo3D_Sample.md) | Demonstrates the conversion of a 2d parameteric space curve into the equivalent 3d model space curve. To use this sample you must have a part open. You can select any face and 3D curves will be drawn on the face using client graphics. |
| [Selection of Surface Graphics Primitives](../../sample-programs/SelectSurfaceGraphicsPrimitives_Sample.md) | This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case). |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |
| [Transient B-Rep Ruled Surface with Lines](../../sample-programs/TransientBRepRuledSurf1_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses all straight line segments for each of the sections. A part document must be open. |
| [Transient B-Rep Ruled Surface with Arc and Line](../../sample-programs/TransientBRepRuledSurf2_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses straight line segments for once section and an arc for the second. A part document must be open. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |