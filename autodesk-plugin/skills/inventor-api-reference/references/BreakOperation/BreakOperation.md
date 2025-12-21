# BreakOperation Object

## Description

A BreakOperation object represents a break applied to a drawing view. Editing or deleting this BreakOperation object will modify all affected views.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../BreakOperation/BreakOperation_Delete.md) | Method that deletes the break operation from the drawing view. The break is deleted from all other affected drawing views as well. |
| [GetReferenceKey](../BreakOperation/BreakOperation_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllAffectedViews](../BreakOperation/BreakOperation_AllAffectedViews.md) | Property that returns all the DrawingView objects affected by this break operation. Multiple drawing views can be affected by a break operation if children views inherit breaks or if the break is propagated up to the parent view. |
| [Application](../BreakOperation/BreakOperation_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../BreakOperation/BreakOperation_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BreakLineSketch](../BreakOperation/BreakOperation_BreakLineSketch.md) | Read-only property that returns the DrawingSketch object containing the break lines. |
| [BreakStyle](../BreakOperation/BreakOperation_BreakStyle.md) | Read-write property that gets and sets the break style. |
| [DisplayLevel](../BreakOperation/BreakOperation_DisplayLevel.md) | Read-write property that gets and sets the appearance of the break lines. |
| [EndPoint](../BreakOperation/BreakOperation_EndPoint.md) | Read-write property that gets and sets the end point of the break in sheet space. |
| [Gap](../BreakOperation/BreakOperation_Gap.md) | Read-write property that gets and sets the gap (in centimeters) between the break lines. |
| [IsSourceBreakOperation](../BreakOperation/BreakOperation_IsSourceBreakOperation.md) | Property that returns whether this break operation is the source for inherited break operations. The property returns True if there are no related break operations. If the property returns False, use the SourceBreakOperation property to find the source break. |
| [Layer](../BreakOperation/BreakOperation_Layer.md) | Gets and sets the layer associated with this object. |
| [MidPoint](../BreakOperation/BreakOperation_MidPoint.md) | Read-write property that gets and sets the midpoint of the break in sheet space. |
| [NumberOfSymbols](../BreakOperation/BreakOperation_NumberOfSymbols.md) | Read-write property that gets and sets the number of break symbols to use for a structural style break. |
| [Orientation](../BreakOperation/BreakOperation_Orientation.md) | Property that returns whether the orientation of the break is horizontal or vertical. Possible return values are kHorizontalBreakOrientation and kVerticalBreakOrientation. |
| [Parent](../BreakOperation/BreakOperation_Parent.md) | Property that returns the parent drawing view from which this BreakOperation was retrieved. |
| [SourceBreakOperation](../BreakOperation/BreakOperation_SourceBreakOperation.md) | Property that returns the source BreakOperation object. For instance, if a projected view inherits the break from the parent base view, this property on the BreakOperation retrieved from the projected view will return the corresponding BreakOperation from the base view. If this BreakOperation itself is the source, the property returns nothing. |
| [StartPoint](../BreakOperation/BreakOperation_StartPoint.md) | Read-write property that gets and sets the start point of the break in sheet space. |
| [Type](../BreakOperation/BreakOperation_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BreakOperation.SourceBreakOperation](../BreakOperation/BreakOperation_SourceBreakOperation.md), [BreakOperations.Add](../BreakOperations/BreakOperations_Add.md), [BreakOperations.AddBySketch](../BreakOperations/BreakOperations_AddBySketch.md), [BreakOperations.Item](../BreakOperations/BreakOperations_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation of a break operation in a drawing view](../../sample-programs/BreakOperations_Add_Sample.md) | Demonstrates the creation of a break operation. |
| [Create BreakOpertion by Sketch Sample](../../sample-programs/CreateBreakOpertionBySketchSample_Sample.md) | This sample demonstrates how to create a break operation using a sketch. |

## Version

Introduced in version 2010
