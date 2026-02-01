# DrawingViews Object

## Description

The DrawingViews collection object provides access to the objects associated with the sheet the collection was obtained from. It also provides method to create new drawing views.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddAssociativeDraftView](../DrawingViews/DrawingViews_AddAssociativeDraftView.md) | Method that creates a new associative draft . An empty draft view is created and associated with the input document. The newly created DrawingView is returned. |
| [AddAuxiliaryView](../DrawingViews/DrawingViews_AddAuxiliaryView.md) | Method that creates an auxiliary drawing view. |
| [AddBaseView](../DrawingViews/DrawingViews_AddBaseView.md) | Method that creates a new base . The newly created DrawingView is returned. |
| [AddDetailView](../DrawingViews/DrawingViews_AddDetailView.md) | Method that creates a detail drawing view. This method fails if the parent sheet is not active. |
| [AddDraftView](../DrawingViews/DrawingViews_AddDraftView.md) | Method that creates a new draft . The newly created DrawingView is returned. |
| [AddOverlayView](../DrawingViews/DrawingViews_AddOverlayView.md) | Method that creates an overlay drawing view. |
| [AddOverlayView2](../DrawingViews/DrawingViews_AddOverlayView2.md) | Method that creates an overlay drawing view. |
| [AddProjectedView](../DrawingViews/DrawingViews_AddProjectedView.md) | Method that creates a projected . |
| [AddSectionView](../DrawingViews/DrawingViews_AddSectionView.md) | Method that creates a section drawing view. |
| [AddSectionView2](../DrawingViews/DrawingViews_AddSectionView2.md) | Method that creates a section drawing view. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Count](../DrawingViews/DrawingViews_Count.md) | Property that returns the number of items in this collection. |
| [Item](../DrawingViews/DrawingViews_Item.md) | Returns the specified object from the collection. |
| [Type](../DrawingViews/DrawingViews_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Sheet.DrawingViews](../Sheet/Sheet_DrawingViews.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create BreakOpertion by Sketch Sample](../../sample-programs/CreateBreakOpertionBySketchSample_Sample.md) | This sample demonstrates how to create a break operation using a sketch. |

## Version

Introduced in version 4
