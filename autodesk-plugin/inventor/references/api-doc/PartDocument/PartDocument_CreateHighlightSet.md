# PartDocument.CreateHighlightSet Method

Parent Object: [PartDocument](../PartDocument/PartDocument.md)

## Description

Method that creates a new highlight set.

## Syntax

PartDocument.**CreateHighlightSet**() As [HighlightSet](../HighlightSet/HighlightSet.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Highlight Feature Faces](../../sample-programs/HighlightSet_Sample.md) | This sample highlights the faces of an extrusion, revolution, or hole feature. It differentiates the faces on the start cap, end cap, and side faces by highlighting them in different colors. The HighlightFeatureFaces sub highlights the feature faces. Since the highlight set objects are declared outside of this sub, the highlighting remains after the sub has finished executing. Use the ClearHighlight sub to clear the highlighting that does so by releasing the HighlightSet objects. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |