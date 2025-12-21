# BreakOutOperation Object

## Description

A BreakOutOperation object represents a break out applied to a drawing view. Editing or deleting this BreakOutOperation object will modify all affected views.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../BreakOutOperation/BreakOutOperation_Delete.md) | Method that deletes the break out operation from the drawing view. The break out is deleted from all other affected drawing views as well. |
| [GetDepth](../BreakOutOperation/BreakOutOperation_GetDepth.md) | Method that returns the information controlling the depth of the break out. |
| [GetReferenceKey](../BreakOutOperation/BreakOutOperation_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [SetDepth](../BreakOutOperation/BreakOutOperation_SetDepth.md) | Method that sets the depth of the break out. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllAffectedViews](../BreakOutOperation/BreakOutOperation_AllAffectedViews.md) | Property that returns all the DrawingView objects affected by this break out operation. Multiple drawing views can be affected by a break out operation if children views inherit break outs. |
| [Application](../BreakOutOperation/BreakOutOperation_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../BreakOutOperation/BreakOutOperation_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DepthType](../BreakOutOperation/BreakOutOperation_DepthType.md) | Property returns how the depth of the break out is defined. To change to another type use the DepthSource property. |
| [DisplayComponentsWithinTheSectionCut](../BreakOutOperation/BreakOutOperation_DisplayComponentsWithinTheSectionCut.md) | Read-write property that gets and sets whether or not to display the components within the section cut. |
| [Parent](../BreakOutOperation/BreakOutOperation_Parent.md) | Property that returns the parent drawing view from which this BreakOutOperation was retrieved. |
| [Profile](../BreakOutOperation/BreakOutOperation_Profile.md) | Read-write property that gets and sets the sketch profile used for the break out. |
| [SectionAllParts](../BreakOutOperation/BreakOutOperation_SectionAllParts.md) | Read-write property that gets and sets whether to section all parts in the break out area. |
| [Type](../BreakOutOperation/BreakOutOperation_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[BreakOutOperations.Add](../BreakOutOperations/BreakOutOperations_Add.md), [BreakOutOperations.Item](../BreakOutOperations/BreakOutOperations_Item.md)

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |