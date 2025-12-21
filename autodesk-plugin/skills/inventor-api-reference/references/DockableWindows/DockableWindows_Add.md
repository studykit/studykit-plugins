# DockableWindows.Add Method

Parent Object: [DockableWindows](../DockableWindows/DockableWindows.md)

## Description

Method that creates a new DockableWindow. The newly created DockableWindow is returned. The window is created invisible and is undocked. The window remains invisible until explicitly made visible by the creator of the window.

## Syntax

DockableWindows.**Add**( ***ClientId*** As String, ***InternalName*** As String, ***Caption*** As String ) As [DockableWindow](../DockableWindow/DockableWindow.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String |  |
| InternalName | String |  |
| Caption | String |  |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Dockable window](../../sample-programs/DockableWindows_Add_Sample.md) | This sample demonstrates creating a dockable window and adding a dialog into it. |

## Version

Introduced in version 2011
