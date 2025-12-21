# UserInterfaceEvents Object

## Description

This object provides notification of environment and command bar reset events.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../UserInterfaceEvents/UserInterfaceEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../UserInterfaceEvents/UserInterfaceEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../UserInterfaceEvents/UserInterfaceEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnEnvironmentChange](../UserInterfaceEvents/UserInterfaceEvents_OnEnvironmentChange.md) | The OnEnvironmentChange event notifies the client when the active environment switches from one environment to another. |
| [OnResetEnvironments](../UserInterfaceEvents/UserInterfaceEvents_OnResetEnvironments.md) | The OnResetEnvironments event notifies the client when environments have been reset. |
| [OnResetInventorLayout](../UserInterfaceEvents/UserInterfaceEvents_OnResetInventorLayout.md) | Event that is fired when the Inventor layout is reset. |
| [OnResetMarkingMenu](../UserInterfaceEvents/UserInterfaceEvents_OnResetMarkingMenu.md) | Event that is fired when the user resets an individual or all radial marking menus. |
| [OnResetRibbonInterface](../UserInterfaceEvents/UserInterfaceEvents_OnResetRibbonInterface.md) | Event that is fired when the ribbon user interface is reset. |
| [OnResetShortcuts](../UserInterfaceEvents/UserInterfaceEvents_OnResetShortcuts.md) | Event that is fired when command shortcuts/aliases are reset in the Customize dialog (using either the "Reset All Keys" or "Reset All" button). |

## Accessed From

[UserInterfaceManager.UserInterfaceEvents](../UserInterfaceManager/UserInterfaceManager_UserInterfaceEvents.md)

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |