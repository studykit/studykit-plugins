# RevolveFeature.StartFaces Property

Parent Object: [RevolveFeature](../RevolveFeature/RevolveFeature.md)

## Description

Property that returns the set of that cap one end of the revolution that are coincident with the sketch plane. In the case of a symmetric revolution these faces are the ones on the positive normal side of the sketch plane. In the cases where there aren't any start faces this property will return Nothing.

## Syntax

RevolveFeature.**StartFaces**() As [Faces](../Faces/Faces.md)

## Property Value

This is a read only property whose value is a [Faces](../Faces/Faces.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Highlight Feature Faces](../../sample-programs/HighlightSet_Sample.md) | This sample highlights the faces of an extrusion, revolution, or hole feature. It differentiates the faces on the start cap, end cap, and side faces by highlighting them in different colors. The HighlightFeatureFaces sub highlights the feature faces. Since the highlight set objects are declared outside of this sub, the highlighting remains after the sub has finished executing. Use the ClearHighlight sub to clear the highlighting that does so by releasing the HighlightSet objects. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |