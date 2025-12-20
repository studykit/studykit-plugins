# DockableWindows Object

## Description

The DockableWindows collection object provides access to all existing dockable windows and provides methods to create additional ones.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../DockableWindows/DockableWindows_Add.md) | Method that creates a new DockableWindow. The newly created DockableWindow is returned. The window is created invisible and is undocked. The window remains invisible until explicitly made visible by the creator of the window. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DockableWindows/DockableWindows_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../DockableWindows/DockableWindows_Count.md) | Property that returns the number of items in the collection. |
| [Events](../DockableWindows/DockableWindows_Events.md) | Property that returns the DockableWindowsEvents object that hosts events related to dockable windows. |
| [Item](../DockableWindows/DockableWindows_Item.md) | Returns the specified DockableWindow object from the collection. |
| [Type](../DockableWindows/DockableWindows_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DockableWindowsEvents.Parent](../DockableWindowsEvents/DockableWindowsEvents_Parent.md), [UserInterfaceManager.DockableWindows](../UserInterfaceManager/UserInterfaceManager_DockableWindows.md)

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