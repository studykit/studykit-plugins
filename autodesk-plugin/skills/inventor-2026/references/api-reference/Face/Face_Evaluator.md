# Face.Evaluator Property

Parent Object: [Face](../Face/Face.md)

## Description

Gets the surface evaluator for this face.

## Syntax

Face.**Evaluator**() As [SurfaceEvaluator](../SurfaceEvaluator/SurfaceEvaluator.md)

## Property Value

This is a read only property whose value is a [SurfaceEvaluator](../SurfaceEvaluator/SurfaceEvaluator.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Basic Selection Using Interaction Events](../../sample-programs/InteractionEventsSink_Sample.md) | This sample demonstrates using the selection events to select a face. Selection is dependent on events and VB only supports events within a class module. |
| [Is cylindrical face interior or exterior?](../../sample-programs/Line_IsColinearTo_Sample.md) | This sample shows how to determine whether the selected cylindircal face is an exterior face or an interior (hollow) face. |
| [3D Curve from Parametric Curve](../../sample-programs/ParameterCurveTo3D_Sample.md) | Demonstrates the conversion of a 2d parameteric space curve into the equivalent 3d model space curve. To use this sample you must have a part open. You can select any face and 3D curves will be drawn on the face using client graphics. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 4
