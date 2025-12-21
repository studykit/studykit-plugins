# TransientBRep.ReadFromFile Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that creates one or more new SurfaceBody objects based on the content of the input file. A SurfaceBodies collection is returned that can contain one or more SurfaceBody object.

## Syntax

TransientBRep.**ReadFromFile**( ***FileName*** As String ) As [SurfaceBodies](../SurfaceBodies/SurfaceBodies.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FileName | String | Input String that defines the full filename of the file to read in. This can be either a SAT, SAB, or a DWG file that contains solids or surfaces. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics from SAT file body](../../sample-programs/GraphicsNode_AddSurfaceGraphics_Sample.md) | The following sample demonstrates how to display client graphics based on bodies read in from a SAT file. |
| [Selection of Surface Graphics Primitives](../../sample-programs/SelectSurfaceGraphicsPrimitives_Sample.md) | This demonstrates the ability to select client graphic primitives, by creating SurfaceGraphics and showing how you can select B-Rep entities within the graphics. You must have a part or assembly open and select a part of sat file which will be read in and displayed as client graphics. Depending on our responses to the program it will create the graphics so that only the node is selectable (which is all that was supported before), so that all of the primitives are selected, or so that only certain primitives are selectable (every other face in this case). |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |