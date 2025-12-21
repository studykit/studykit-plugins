# DockableWindow.AddChild Method

Parent Object: [DockableWindow](../DockableWindow/DockableWindow.md)

## Description

Method that adds a dialog or a control to the dockable window. Currently, you can only add a single child to a dockable window. So this method returns a failure if the dockable window already has a child. It is the responsibility of the client to destroy the dialog/control as and when appropriate.

## Syntax

DockableWindow.**AddChild**( ***Identifier*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Identifier | Variant | Input Variant that specifies the dialog or control. This can either be the HWND of a dialog/window, or the ProgID of a control or the GUID of the control as a string (including the braces "{ }"). The ProgID/GUID can be that of an ActiveX or a .NET user control. |

## Notes

When adding a dialog (by passing in an HWND as input), it must be created as a modeless dialog. Also, it is recommended that the dialog be created with the DockableWindow.HWND as the parent before calling this method. However, if created with any other parent, this method re-parents the child dialog to the dockable window.

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |