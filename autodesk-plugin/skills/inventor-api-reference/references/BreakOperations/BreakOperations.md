# BreakOperations Object

## Description

The BreakOperations collection object contains information about all the break operations applied to a drawing view as well as methods to add breaks to the view.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../BreakOperations/BreakOperations_Add.md) | Method that adds a break to a drawing view. The newly created BreakOperation object is returned. |
| [AddBySketch](../BreakOperations/BreakOperations_AddBySketch.md) | Method that adds a break to a drawing view. The newly created BreakOperation object is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BreakOperations/BreakOperations_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../BreakOperations/BreakOperations_Count.md) | Property that returns the number of items in the collection. |
| [Item](../BreakOperations/BreakOperations_Item.md) | Method that returns the specified break operation object from the collection. |
| [Type](../BreakOperations/BreakOperations_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DetailDrawingView.BreakOperations](../DetailDrawingView/DetailDrawingView_BreakOperations.md), [DrawingView.BreakOperations](../DrawingView/DrawingView_BreakOperations.md), [SectionDrawingView.BreakOperations](../SectionDrawingView/SectionDrawingView_BreakOperations.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation of a break operation in a drawing view](../../sample-programs/BreakOperations_Add_Sample.md) | Demonstrates the creation of a break operation. |
| [Create BreakOpertion by Sketch Sample](../../sample-programs/CreateBreakOpertionBySketchSample_Sample.md) | This sample demonstrates how to create a break operation using a sketch. |

## Version

Introduced in version 2010
