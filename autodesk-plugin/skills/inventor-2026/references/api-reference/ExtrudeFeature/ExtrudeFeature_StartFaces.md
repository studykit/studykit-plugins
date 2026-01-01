# ExtrudeFeature.StartFaces Property

Parent Object: [ExtrudeFeature](../ExtrudeFeature/ExtrudeFeature.md)

## Description

Property that returns the set of that cap one end of the extrusion and are coincident with the sketch plane. In the case of a symmetric extrusion these faces are the ones on the positive normal side of the sketch plane. In the case where there aren't any start faces this property will return Nothing.

## Syntax

ExtrudeFeature.**StartFaces**() As [Faces](../Faces/Faces.md)

## Property Value

This is a read only property whose value is a [Faces](../Faces/Faces.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Extrude Feature - Create Block with Pocket](../../sample-programs/ExtrudeFeature_Sample.md) | This sample demonstrates creating a simple solid consisting a block with a pocket. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Fillet Feature (Complex)](../../sample-programs/FilletFeature2_Sample.md) | This sample demonstrates creating a complex fillet. The result in this case has several different constant radii fillets and two edges that use variable radius, with one of these having a different radius defined along the edge. |
| [Fillet Feature (Simple)](../../sample-programs/FilletFeature3_Sample.md) | This sample demonstrates using the AddSimple method of the FilletFeatures collection to create a constant radius fillet. |
| [Highlight Feature Faces](../../sample-programs/HighlightSet_Sample.md) | This sample highlights the faces of an extrusion, revolution, or hole feature. It differentiates the faces on the start cap, end cap, and side faces by highlighting them in different colors. The HighlightFeatureFaces sub highlights the feature faces. Since the highlight set objects are declared outside of this sub, the highlighting remains after the sub has finished executing. Use the ClearHighlight sub to clear the highlighting that does so by releasing the HighlightSet objects. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |

## Version

Introduced in version 5
