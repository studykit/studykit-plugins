# ViewTabGroup.MoveToGroup Method

Parent Object: [ViewTabGroup](../ViewTabGroup/ViewTabGroup.md)

## Description

Method that moves the current ViewTabGroup to another ViewTabGroup. The ViewTabGroup the current ViewTabGroup moves into will be returned.

## Syntax

ViewTabGroup.**MoveToGroup**( ***TargetViewTab*** As [ViewTab](../ViewTab/ViewTab.md), ***DockingState*** As [DockingStateEnum](../DockingStateEnum.md) ) As [ViewTabGroup](../ViewTabGroup/ViewTabGroup.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetViewTab | [ViewTab](../ViewTab/ViewTab.md) | Input ViewTab object that specifies the target ViewTab. |
| DockingState | [DockingStateEnum](../DockingStateEnum.md) | Input DockingStateEnum value that specifies the docking state of the current ViewTabGroup. Valid values for this argument are: kDockLeft and kDockRight. |

## Version

Introduced in version 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |