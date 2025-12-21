# ViewTab.MoveToGroup Method

Parent Object: [ViewTab](../ViewTab/ViewTab.md)

## Description

Method that moves the current view tab to a ViewTabGroup. The ViewTabGroup the current ViewTab moves into will be returned.

## Syntax

ViewTab.**MoveToGroup**( ***CreateNewGroup*** As Boolean, ***TargetViewTab*** As [ViewTab](../ViewTab/ViewTab.md), ***DockingState*** As [DockingStateEnum](../DockingStateEnum.md), [***AdditionalViewTabs***] As Variant ) As [ViewTabGroup](../ViewTabGroup/ViewTabGroup.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CreateNewGroup | Boolean | Input Boolean value that specifies whether to move the current ViewTab to a newly created ViewTabGroup or an existing ViewTabGroup. If set this as True then a new ViewTabGroup containing this ViewTab will be created. If this is set to False current ViewTab will be moved to an existing ViewTabGroup that contains the TargetViewTab. |
| TargetViewTab | [ViewTab](../ViewTab/ViewTab.md) | Input ViewTab object that specifies the target ViewTab. |
| DockingState | [DockingStateEnum](../DockingStateEnum.md) | Input DockingStateEnum value that specifies the docking state of the current ViewTab. If the CreateNewGroup is set to True then the current ViewTab will be docked to the location against the TargetViewTab’s group, valid values for this argument are: kDockBottom, kDockTop, kDockLeft and kDockRight. If the CreateNewGroup is set to False, then the current ViewTab will be moved to the left or right side of the TargetViewTab, so valid values for this argument are: kDockLeft and kDockRight. |
| AdditionalViewTabs | Variant | Optional input ObjectCollection object containing ViewTab objects as additional view tabs to move to the group with current ViewTab. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Move view tab between different view frames](../../sample-programs/ViewTabMoveSample_Sample.md) | This sample demonstrates how to move views using ViewTab between different view frames. |

## Version

Introduced in version 2022
