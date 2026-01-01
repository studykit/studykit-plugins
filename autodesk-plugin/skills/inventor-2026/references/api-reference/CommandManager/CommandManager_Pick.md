# CommandManager.Pick Method

Parent Object: [CommandManager](../CommandManager/CommandManager.md)

## Description

Method that allows the user to pick a single entity.

## Syntax

CommandManager.**Pick**( ***Filter*** As [SelectionFilterEnum](../SelectionFilterEnum.md), ***PromptText*** As String ) As Object

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Filter | [SelectionFilterEnum](../SelectionFilterEnum.md) | SelectionFilterEnum Entity filter |
| PromptText | String | Text to display as prompt. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Approximate Polyline to 3D Curve](../../sample-programs/Approximate3DSketchGeometry_Sample.md) | Draws a polyline that is an approximation of the selected curve. To use this have a part open that contains a 3D skech that contains curves. |
| [Single selection - simple](../../sample-programs/CommandManager_Pick_Sample.md) | The following sample demonstrates getting a single selection from the user. |
| [Replace content center part](../../sample-programs/ContentCenterPartReplace_Sample.md) | This sample demonstrates how to replace the content part referenced by an assembly occurrence. |
| [Extract a Partial Curve from a Curve](../../sample-programs/ExtractPartial2DCurves_Sample.md) | Demonstrates the ability to extract partial curves from a transient geometry curve. This sample has you select an existing sketch spline and extracts three curves from the curve. It then creates real curves using the extracted curves and deletes the original sketch curve. |
| [Copy sketch contents](../../sample-programs/Sketch_CopyContentsTo_Sample.md) | This sample shows how to copy the contents of one sketch to another. |
| [Split a 2D Curve](../../sample-programs/Split2DCurve_Sample.md) | Demonstrates the ability to extract split curves from a transient geometry curve. This sample has you select an existing sketch spline and splits it at the midpoint of parametric space. It then creates real curves using the split curve results and deletes the original sketch curve. |

## Version

Introduced in version 2011
