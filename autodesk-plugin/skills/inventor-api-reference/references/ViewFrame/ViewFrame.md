# ViewFrame Object

## Description

ViewFrame Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Arrange](../ViewFrame/ViewFrame_Arrange.md) | Method that tiles the views in the view frame window. |
| [Close](../ViewFrame/ViewFrame_Close.md) | Method that closes this view frame. |
| [Close2](../ViewFrame/ViewFrame_Close2.md) | Method that closes this view frame. Close a ViewFrame may cause documents to close, use the argument to specify the documents to save if necessary. This does nothing if try to close the default ViewFrame. |
| [Move](../ViewFrame/ViewFrame_Move.md) | Method that moves the view frame window. |
| [RestorePreviousLayout](../ViewFrame/ViewFrame_RestorePreviousLayout.md) | Method that restores the previous layout for this view frame window. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ViewFrame/ViewFrame_Application.md) | Read-only property that returns the root Application object. |
| [Caption](../ViewFrame/ViewFrame_Caption.md) | Read-only property that returns the caption of this view frame. |
| [Height](../ViewFrame/ViewFrame_Height.md) | Read-write property that gets and sets the height of the view frame. |
| [IsDefault](../ViewFrame/ViewFrame_IsDefault.md) | Read-only property that returns whether this view frame is the default one. |
| [Left](../ViewFrame/ViewFrame_Left.md) | Read-only property that returns the distance between the left edge of the screen and left edge of the view frame. |
| [Parent](../ViewFrame/ViewFrame_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Top](../ViewFrame/ViewFrame_Top.md) | Read-only property that returns the distance between the top edge of the screen and top edge of the view frame. |
| [Type](../ViewFrame/ViewFrame_Type.md) | Read-only property returning kViewFrameObject indicating this object’s type. |
| [ViewTabGroups](../ViewFrame/ViewFrame_ViewTabGroups.md) | Read-only property that returns the ViewTabGroupsEnumerator collection object. |
| [ViewTabs](../ViewFrame/ViewFrame_ViewTabs.md) | Read-only property that returns the view tabs that are located in this view frame. |
| [Width](../ViewFrame/ViewFrame_Width.md) | Read-write property that gets and sets the width of the view frame. |
| [WindowState](../ViewFrame/ViewFrame_WindowState.md) | Read-write property that gets and sets the window state of this view frame. |

## Accessed From

[Application.ActiveViewFrame](../Application/Application_ActiveViewFrame.md), [View.ViewFrame](../View/View_ViewFrame.md), [ViewFramesEnumerator.Item](../ViewFramesEnumerator/ViewFramesEnumerator_Item.md), [ViewTab.MoveToNewViewFrame](../ViewTab/ViewTab_MoveToNewViewFrame.md), [ViewTab.ViewFrame](../ViewTab/ViewTab_ViewFrame.md), [ViewTabGroup.MoveToNewViewFrame](../ViewTabGroup/ViewTabGroup_MoveToNewViewFrame.md), [ViewTabGroup.ViewFrame](../ViewTabGroup/ViewTabGroup_ViewFrame.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Dock browser pane to a custom ViewFrame](../../sample-programs/DockBrowserPaneSample_Sample.md) | This sample demonstrates how to dock the browser pane to a custom ViewFrame. |
| [Move view tab between different view frames](../../sample-programs/ViewTabMoveSample_Sample.md) | This sample demonstrates how to move views using ViewTab between different view frames. |

## Version

Introduced in version 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |