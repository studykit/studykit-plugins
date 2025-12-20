# DockableWindows.Item Property

Parent Object: [DockableWindows](../DockableWindows/DockableWindows.md)

## Description

Returns the specified DockableWindow object from the collection.

## Syntax

DockableWindows.**Item**( ***Index*** As Variant ) As [DockableWindow](../DockableWindow/DockableWindow.md)

## Property Value

This is a read only property whose value is a [DockableWindow](../DockableWindow/DockableWindow.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the DockableWindow to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the InternalName of the window. If an out of range index or an InternalName of a non-existent DockableWindow is provided, an error will occur. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |