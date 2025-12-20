# HighlightSet.Color Property

Parent Object: [HighlightSet](../HighlightSet/HighlightSet.md)

## Description

Gets/Sets the color of the highlight set.

## Syntax

HighlightSet.**Color**() As [Color](../Color/Color.md)

## Property Value

This is a read/write property whose value is a [Color](../Color/Color.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Interference Analysis](../../sample-programs/AssemblyComponentDefinition_AnalyzeInterference_Sample.md) | This sample demonstrates the functions used to calculate interference analysis in an assembly. |
| [Creating a HighlightSet](../../sample-programs/Document_CreateHighlightSet_Sample.md) | Demonstrates creating a highlight set. |
| [Highlight Feature Faces](../../sample-programs/HighlightSet_Sample.md) | This sample highlights the faces of an extrusion, revolution, or hole feature. It differentiates the faces on the start cap, end cap, and side faces by highlighting them in different colors. The HighlightFeatureFaces sub highlights the feature faces. Since the highlight set objects are declared outside of this sub, the highlighting remains after the sub has finished executing. Use the ClearHighlight sub to clear the highlighting that does so by releasing the HighlightSet objects. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |