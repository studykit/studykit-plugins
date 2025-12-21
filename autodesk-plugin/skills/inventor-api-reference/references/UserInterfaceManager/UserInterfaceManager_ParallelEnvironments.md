# UserInterfaceManager.ParallelEnvironments Property

Parent Object: [UserInterfaceManager](../UserInterfaceManager/UserInterfaceManager.md)

## Description

Property that returns the list of Environments valid for the edit target or the environment being switched to. Environments can be added to or removed from the list as seen appropriate by the client when an OnNewEditObject or an OnEnvironmentChange event is received. This list of environments will show in the Applications menu item. This list may only contain non-built-in environments.

## Syntax

UserInterfaceManager.**ParallelEnvironments**() As [EnvironmentList](../EnvironmentList/EnvironmentList.md)

## Property Value

This is a read only property whose value is an [EnvironmentList](../EnvironmentList/EnvironmentList.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |