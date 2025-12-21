# PartDocument.SelectSet Property

Parent Object: [PartDocument](../PartDocument/PartDocument.md)

## Description

Property that returns the SelectSet object.

## Syntax

PartDocument.**SelectSet**() As [SelectSet](../SelectSet/SelectSet.md)

## Property Value

This is a read only property whose value is a [SelectSet](../SelectSet/SelectSet.md).

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