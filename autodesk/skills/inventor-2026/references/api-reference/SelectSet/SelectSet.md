# SelectSet Object

## Description

The SelectSet object acts as a container for all of the objects that are currently selected using the Select command. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Clear](../SelectSet/SelectSet_Clear.md) | Method that removes all objects from the select set. |
| [Delete](../SelectSet/SelectSet_Delete.md) | Method that deletes all deletable objects in the select set. This is the equivalent of the Delete command. Not all objects that are selectable can be deleted. For example, you can select an edge, but it cannot be deleted. Any undeletable objects in the select set are ignored. |
| [Remove](../SelectSet/SelectSet_Remove.md) | Method that removes the specified object from the select set. |
| [Select](../SelectSet/SelectSet_Select.md) | Method that adds an entity to the select set. |
| [SelectMultiple](../SelectSet/SelectSet_SelectMultiple.md) | Adds multiple entities to the select set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Count](../SelectSet/SelectSet_Count.md) | Property that returns the number of objects in the select set. |
| [Item](../SelectSet/SelectSet_Item.md) | Returns the specified object from the select set. |
| [Type](../SelectSet/SelectSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyDocument.SelectSet](../AssemblyDocument/AssemblyDocument_SelectSet.md), [Document.SelectSet](../Document/Document_SelectSet.md), [DrawingDocument.SelectSet](../DrawingDocument/DrawingDocument_SelectSet.md), [PartDocument.SelectSet](../PartDocument/PartDocument_SelectSet.md), [PresentationDocument.SelectSet](../PresentationDocument/PresentationDocument_SelectSet.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Interference Analysis](../../sample-programs/AssemblyComponentDefinition_AnalyzeInterference_Sample.md) | This sample demonstrates the functions used to calculate interference analysis in an assembly. |
| [Add mate constraint with limits](../../sample-programs/AssemblyConstraints_AddMateConstraint3_Sample.md) | This sample demonstrates the creation of an assembly mate constraint with maximum and minimum limits defined. |
| [Find component referenced by balloon](../../sample-programs/BalloonValueSet_ReferencedRow_Sample.md) | This sample demonstrates how to find the component that a balloon references. |
| [Create bend note](../../sample-programs/BendNotes_Add_Sample.md) | This sample demonstrates the creation of a bend note on the drawing view of a flat pattern. |
| [Creation of a break operation in a drawing view](../../sample-programs/BreakOperations_Add_Sample.md) | Demonstrates the creation of a break operation. |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |
| [Client Graphics - Draw Range Box](../../sample-programs/ClientGraphics_Sample.md) | This sample demonstrates the use of client graphics to draw the range box of selected entities. |
| [Copy a sketch](../../sample-programs/CopySketch_Sample.md) | This sample demonstrates copying the contents of a sketch into another sketch via the API. |
| [Adding and editing a feature control frame](../../sample-programs/FeatureControlFrame_FeatureControlFrameRows_Sample.md) | These samples demonstrate editing an existing feature control frame symbol. The first sample adds a row to an existing symbol. The second sample replaces all rows of an existing symbol. |
| [Highlight Feature Faces](../../sample-programs/HighlightSet_Sample.md) | This sample highlights the faces of an extrusion, revolution, or hole feature. It differentiates the faces on the start cap, end cap, and side faces by highlighting them in different colors. The HighlightFeatureFaces sub highlights the feature faces. Since the highlight set objects are declared outside of this sub, the highlighting remains after the sub has finished executing. Use the ClearHighlight sub to clear the highlighting that does so by releasing the HighlightSet objects. |
| [Create thread note](../../sample-programs/HoleThreadNotes_Add_Sample.md) | This sample demonstrates the creation of a thread note on a drawing view. |
| [create punch note](../../sample-programs/PunchNotes_Add_Sample.md) | This sample demonstrates the creation of a punch note on the drawing view of a flat pattern. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |
| [Break alignment of a section view](../../sample-programs/SectionDrawingView_Sample.md) | Sample showing how to break the alignment of a drawing section view by calling the DrawingBreakViewAlignment command. |
| [Sketch Display Entities](../../sample-programs/SketchEntity_Sample.md) | This sample demonstrates the query functionality available for sketch entities. |
| [Add surface texture symbol to dimension](../../sample-programs/SurfaceTextureSymbols_Add_Sample.md) | This sample demonstrates the creation of a surface texture symbol attached to the extension line of a drawing dimension. |
| [Assembly Move Occurrence](../../sample-programs/TransformOccurrence_Sample.md) | This sample demonstrates moving a component occurrence. This sample performs a translate, but a rotate can also be performed since the transform is defined using a matrix. |
| [OnDrag Event - dragging a WorkPoint](../../sample-programs/UserInputEventsSink_OnDrag_Sample.md) | This sample demonstrates the use of the OnDrag event to drag fixed work points when no command is active. This sample only allows drags parallel to the X-Y plane. This sample is dependent on events and VB only supports events within a class module. |

## Version

Introduced in version 5
