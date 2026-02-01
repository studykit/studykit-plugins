# DockableWindowsEvents Object

## Description

DockableWindows events object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DockableWindowsEvents/DockableWindowsEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../DockableWindowsEvents/DockableWindowsEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../DockableWindowsEvents/DockableWindowsEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnHelp](../DockableWindowsEvents/DockableWindowsEvents_OnHelp.md) | Fires whenever the user clicks the help button in a dockable window. |
| [OnHide](../DockableWindowsEvents/DockableWindowsEvents_OnHide.md) | Fires whenever a dockable window is hidden (i.e. closed). |
| [OnShow](../DockableWindowsEvents/DockableWindowsEvents_OnShow.md) | Fires whenever a dockable window is shown. |

## Accessed From

[DockableWindows.Events](../DockableWindows/DockableWindows_Events.md)

## Version

Introduced in version 2012
