# Face.EdgeLoops Property

Parent Object: [Face](../Face/Face.md)

## Description

Gets the EdgeLoops collection referenced by this Face.

## Syntax

Face.**EdgeLoops**() As [EdgeLoops](../EdgeLoops/EdgeLoops.md)

## Property Value

This is a read only property whose value is an [EdgeLoops](../EdgeLoops/EdgeLoops.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |