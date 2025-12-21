# DockableWindow.GetDockingState Method

Parent Object: [DockableWindow](../DockableWindow/DockableWindow.md)

## Description

Method that gets the docking state of the dockable window.

## Syntax

DockableWindow.**GetDockingState**( ***DockingState*** As [DockingStateEnum](../DockingStateEnum.md), ***DockToObject*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DockingState | [DockingStateEnum](../DockingStateEnum.md) | Output DockingStateEnum value that indicates the docking state. |
| DockToObject | Object | Output object to indicate where the browser pane docks to. This returns Nothing if the DockingState returns kFloat. |

## Version

Introduced in version 2022
