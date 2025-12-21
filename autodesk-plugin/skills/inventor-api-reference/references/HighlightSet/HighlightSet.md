# HighlightSet Object

## Description

The HighlightSet object defines a set of objects and an associated color to display them with.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddItem](../HighlightSet/HighlightSet_AddItem.md) | Method that adds an entity to the highlight set. |
| [AddMultipleItems](../HighlightSet/HighlightSet_AddMultipleItems.md) | Adds multiple entities to the highlight set. |
| [Clear](../HighlightSet/HighlightSet_Clear.md) | Method that removes all objects from the highlight set. |
| [Delete](../HighlightSet/HighlightSet_Delete.md) | Method that deletes the HighlightSet object. |
| [Remove](../HighlightSet/HighlightSet_Remove.md) | Method that removes the specified object from the highlight set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Color](../HighlightSet/HighlightSet_Color.md) | Gets/Sets the color of the highlight set. |
| [Count](../HighlightSet/HighlightSet_Count.md) | Property that returns the number of objects in the highlight set. |
| [Item](../HighlightSet/HighlightSet_Item.md) | Returns the specified object from the highlight set. |
| [Type](../HighlightSet/HighlightSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ApprenticeServerDocument.CreateHighlightSet](../ApprenticeServerDocument/ApprenticeServerDocument_CreateHighlightSet.md), [ApprenticeServerDrawingDocument.CreateHighlightSet](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_CreateHighlightSet.md), [AssemblyDocument.CreateHighlightSet](../AssemblyDocument/AssemblyDocument_CreateHighlightSet.md), [Document.CreateHighlightSet](../Document/Document_CreateHighlightSet.md), [DrawingDocument.CreateHighlightSet](../DrawingDocument/DrawingDocument_CreateHighlightSet.md), [HighlightSets.Add](HighlightSets_Add.md), [HighlightSets.Item](HighlightSets_Item.md), [PartDocument.CreateHighlightSet](../PartDocument/PartDocument_CreateHighlightSet.md), [PresentationDocument.CreateHighlightSet](../PresentationDocument/PresentationDocument_CreateHighlightSet.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Interference Analysis](../../sample-programs/AssemblyComponentDefinition_AnalyzeInterference_Sample.md) | This sample demonstrates the functions used to calculate interference analysis in an assembly. |
| [Creating a HighlightSet](../../sample-programs/Document_CreateHighlightSet_Sample.md) | Demonstrates creating a highlight set. |
| [Highlight Feature Faces](../../sample-programs/HighlightSet_Sample.md) | This sample highlights the faces of an extrusion, revolution, or hole feature. It differentiates the faces on the start cap, end cap, and side faces by highlighting them in different colors. The HighlightFeatureFaces sub highlights the feature faces. Since the highlight set objects are declared outside of this sub, the highlighting remains after the sub has finished executing. Use the ClearHighlight sub to clear the highlighting that does so by releasing the HighlightSet objects. |

## Version

Introduced in version 5
