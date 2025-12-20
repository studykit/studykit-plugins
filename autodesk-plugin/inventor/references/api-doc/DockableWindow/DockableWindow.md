# DockableWindow Object

## Description

A DockableWindow object represents a window that can be docked on to the Inventor application window by the user.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddChild](../DockableWindow/DockableWindow_AddChild.md) | Method that adds a dialog or a control to the dockable window. Currently, you can only add a single child to a dockable window. So this method returns a failure if the dockable window already has a child. It is the responsibility of the client to destroy the dialog/control as and when appropriate. |
| [Clear](../DockableWindow/DockableWindow_Clear.md) | Method that empties the contents of the dockable window (i.e. removes any children of the window). This does not destroy the child dialog/controls; it is the responsibility of the client to destroy them. |
| [Delete](../DockableWindow/DockableWindow_Delete.md) | Method that deletes the DockableWindow. This does not destroy the child dialog/controls; it is the responsibility of the client to destroy them. |
| [GetDockingState](../DockableWindow/DockableWindow_GetDockingState.md) | Method that gets the docking state of the dockable window. |
| [Move](../DockableWindow/DockableWindow_Move.md) | Method that repositions and resizes the window. If the window is docked, calling this method automatically undocks the window and honors the input values. |
| [SetDockingState](../DockableWindow/DockableWindow_SetDockingState.md) | Method that set the docking state of the window. |
| [SetMinimumSize](../DockableWindow/DockableWindow_SetMinimumSize.md) | Method that sets the minimum size that the user can resize the window to. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DockableWindow/DockableWindow_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Caption](../DockableWindow/DockableWindow_Caption.md) | Gets and sets the caption of the window. |
| [ClientId](../DockableWindow/DockableWindow_ClientId.md) | Property that returns the string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. '{C9A6C580-3817-11D0-BE4E-080036E87B02}'. |
| [Control](../DockableWindow/DockableWindow_Control.md) | Property that returns the control associated with the pane. This property returns Nothing if the pane contains a dialog and not a control. |
| [DisableCloseButton](../DockableWindow/DockableWindow_DisableCloseButton.md) | Gets and sets whether to disable close button. |
| [DisabledDockingStates](../DockableWindow/DockableWindow_DisabledDockingStates.md) | Read-write property that gets and sets the bit-mask that specifies the docking positions to disallow. |
| [Height](../DockableWindow/DockableWindow_Height.md) | Gets and sets the current height of the window. |
| [HWND](../DockableWindow/DockableWindow_HWND.md) | Property that returns the handle of the dockable window. |
| [InternalName](../DockableWindow/DockableWindow_InternalName.md) | Property that returns the unique internal name of the window. |
| [IsCustomized](../DockableWindow/DockableWindow_IsCustomized.md) | Property that returns whether size, position and docking states of this window have previously been customized and remembered by Inventor. If this property returns True, the size, position and docking states should not be initialized by the creating application so that the last known values are re-applied. |
| [Left](../DockableWindow/DockableWindow_Left.md) | Property that returns the distance between the left edge of the screen and left edge of the window. |
| [Parent](../DockableWindow/DockableWindow_Parent.md) | Property that returns the parent UserInterfaceManager object. |
| [ShowVisibilityCheckBox](../DockableWindow/DockableWindow_ShowVisibilityCheckBox.md) | Gets and sets whether to display the visibility check box in the User Interface dropdown in the View tab | Windows panel. |
| [Top](../DockableWindow/DockableWindow_Top.md) | Property that returns the distance between the top of the screen and top of the window. |
| [Type](../DockableWindow/DockableWindow_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [VisibilityControl](../DockableWindow/DockableWindow_VisibilityControl.md) | Property that returns the button control automatically created by Inventor to control the visibility of the dockable window. |
| [Visible](../DockableWindow/DockableWindow_Visible.md) | Read-write property that gets and sets whether the window is currently visible. |
| [Width](../DockableWindow/DockableWindow_Width.md) | Gets and sets the current width of the window. |

## Accessed From

[DockableWindows.Add](../DockableWindows/DockableWindows_Add.md), [DockableWindows.Item](../DockableWindows/DockableWindows_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Dockable window](../../sample-programs/DockableWindows_Add_Sample.md) | This sample demonstrates creating a dockable window and adding a dialog into it. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |