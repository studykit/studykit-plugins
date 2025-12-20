# Document.SelectSet Property

Parent Object: [Document](../Document/Document.md)

## Description

Property that returns the SelectSet object.

## Syntax

Document.**SelectSet**() As [SelectSet](../SelectSet/SelectSet.md)

## Property Value

This is a read only property whose value is a [SelectSet](../SelectSet/SelectSet.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add assembly insert constraint](../../sample-programs/AssemblyConstraints_AddInsertConstraint_Sample.md) | This sample demonstrates the creation of an assembly insert constraint. |
| [Add assembly mate constraint](../../sample-programs/AssemblyConstraints_AddMateConstraint_Sample.md) | This sample demonstrates the creation of an assembly mate constraint. |
| [Add mate constraint using work planes in parts](../../sample-programs/AssemblyConstraints_AddMateConstraint2_Sample.md) | This sample demonstrates creating a mate constraint between two occurrences using the work planes within those occurrences. |
| [Add mate constraint with limits](../../sample-programs/AssemblyConstraints_AddMateConstraint3_Sample.md) | This sample demonstrates the creation of an assembly mate constraint with maximum and minimum limits defined. |
| [Find component referenced by balloon](../../sample-programs/BalloonValueSet_ReferencedRow_Sample.md) | This sample demonstrates how to find the component that a balloon references. |
| [Highlight Feature Faces](../../sample-programs/HighlightSet_Sample.md) | This sample highlights the faces of an extrusion, revolution, or hole feature. It differentiates the faces on the start cap, end cap, and side faces by highlighting them in different colors. The HighlightFeatureFaces sub highlights the feature faces. Since the highlight set objects are declared outside of this sub, the highlighting remains after the sub has finished executing. Use the ClearHighlight sub to clear the highlighting that does so by releasing the HighlightSet objects. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |