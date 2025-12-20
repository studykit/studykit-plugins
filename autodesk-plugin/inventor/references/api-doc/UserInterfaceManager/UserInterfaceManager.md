# UserInterfaceManager Object

## Description

The UserInterfaceManager object, through which all UI customization objects can be accessed. See [Ribbon Customization](RibbonUI_Overview.md) for an overview.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AllReferencedControls](../UserInterfaceManager/UserInterfaceManager_AllReferencedControls.md) | Method that returns all command controls in Inventor's ribbon interface that reference the input ControlDefinition. Controls from ribbons panels, Quick Access Toolbar and the File Browser (application menu) are returned. |
| [DoEvents](../UserInterfaceManager/UserInterfaceManager_DoEvents.md) | Allows Inventor to process all Windows messages currently in the message queue. |
| [GetCommandPaths](../UserInterfaceManager/UserInterfaceManager_GetCommandPaths.md) | Method that returns all the paths that the given command is found in, optionally filtered to an environment. |
| [ResetRibbonInterface](../UserInterfaceManager/UserInterfaceManager_ResetRibbonInterface.md) | Method that removes all customizations from the ribbon user interface. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveEnvironment](../UserInterfaceManager/UserInterfaceManager_ActiveEnvironment.md) | Property that returns the Environment that is currently active. |
| [Application](../UserInterfaceManager/UserInterfaceManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BalloonTips](../UserInterfaceManager/UserInterfaceManager_BalloonTips.md) | Read-only property that returns the BalloonTips collection object. |
| [CapacityMeterEnabled](../UserInterfaceManager/UserInterfaceManager_CapacityMeterEnabled.md) | Gets and sets whether to enable the capacity meter display in Inventor's status bar. |
| [DockableWindows](../UserInterfaceManager/UserInterfaceManager_DockableWindows.md) | Property that returns the DockableWindows collection object. |
| [Environments](../UserInterfaceManager/UserInterfaceManager_Environments.md) | Property that returns the Environments collection object. |
| [ExpertMode](../UserInterfaceManager/UserInterfaceManager_ExpertMode.md) | Gets/Sets the Boolean flag indicating whether the UI is in Expert mode. |
| [FileBrowserControls](../UserInterfaceManager/UserInterfaceManager_FileBrowserControls.md) | Property that returns a CommandControls collection containing the controls in the File Browser (a.k.a Application Menu). |
| [HelpControls](../UserInterfaceManager/UserInterfaceManager_HelpControls.md) | Property that returns a CommandControls collection containing the controls in the Help Menu. |
| [OverflowMenuBehavior](../UserInterfaceManager/UserInterfaceManager_OverflowMenuBehavior.md) | Read-write property that gets and sets the behavior of the overflow menu. |
| [ParallelEnvironments](../UserInterfaceManager/UserInterfaceManager_ParallelEnvironments.md) | Property that returns the list of Environments valid for the edit target or the environment being switched to. Environments can be added to or removed from the list as seen appropriate by the client when an OnNewEditObject or an OnEnvironmentChange event is received. This list of environments will show in the Applications menu item. This list may only contain non-built-in environments. |
| [Parent](../UserInterfaceManager/UserInterfaceManager_Parent.md) | Property that returns the parent object from whom this object can logically be reached. |
| [PinMiniToolbarPosition](../UserInterfaceManager/UserInterfaceManager_PinMiniToolbarPosition.md) | Read-only property that gets whether the MiniToolbar position is pinned or not. |
| [RibbonAppearance](../UserInterfaceManager/UserInterfaceManager_RibbonAppearance.md) | Gets and sets the appearance of the ribbon. |
| [RibbonDockingState](../UserInterfaceManager/UserInterfaceManager_RibbonDockingState.md) | Gets and sets the docking state of the ribbon. |
| [Ribbons](../UserInterfaceManager/UserInterfaceManager_Ribbons.md) | Property that returns the Ribbons collection object. |
| [RibbonState](../UserInterfaceManager/UserInterfaceManager_RibbonState.md) | Gets and sets the display state of the ribbon. Valid values are kFullRibbon, kMinimizeToTabs, kMinimizeToPanelTitles and kMinimizeToPanelButtons. |
| [ShowBrowser](../UserInterfaceManager/UserInterfaceManager_ShowBrowser.md) | Show/Hide Browser. |
| [ShowCleanScreen](../UserInterfaceManager/UserInterfaceManager_ShowCleanScreen.md) | Gets sets whether the viewed screen area is maximized. |
| [ShowDocumentTabs](../UserInterfaceManager/UserInterfaceManager_ShowDocumentTabs.md) | Gets and sets whether document tabs are displayed. |
| [ShowMarkingMenu](../UserInterfaceManager/UserInterfaceManager_ShowMarkingMenu.md) | Property that gets and sets whether to use the marking menu. |
| [ShowNavigationBar](../UserInterfaceManager/UserInterfaceManager_ShowNavigationBar.md) | Read-write property that gets and sets whether the navigation bar is displayed. |
| [ShowQuickAccessControlsBelowRibbon](../UserInterfaceManager/UserInterfaceManager_ShowQuickAccessControlsBelowRibbon.md) | Gets and sets whether the Quick Access Toolbar (QAT) is shown below or above the ribbon. |
| [ShowStatusBar](../UserInterfaceManager/UserInterfaceManager_ShowStatusBar.md) | Show/Hide StatusBar. |
| [ShowSteeringWheel](../UserInterfaceManager/UserInterfaceManager_ShowSteeringWheel.md) | Read-write property that gets and sets whether the steering wheel control is displayed. |
| [ShowViewCube](../UserInterfaceManager/UserInterfaceManager_ShowViewCube.md) | Read-write property that gets and sets whether the view cube is displayed. |
| [Type](../UserInterfaceManager/UserInterfaceManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UserInteractionDisabled](../UserInterfaceManager/UserInterfaceManager_UserInteractionDisabled.md) | Enable/Disable user interaction. |
| [UserInterfaceEvents](../UserInterfaceManager/UserInterfaceManager_UserInterfaceEvents.md) | Property returning the UserInterfaceEvents object. |

## Accessed From

[Application.UserInterfaceManager](../Application/Application_UserInterfaceManager.md), [BalloonTip.Parent](../BalloonTip/BalloonTip_Parent.md), [DockableWindow.Parent](../DockableWindow/DockableWindow_Parent.md), [Ribbon.Parent](../Ribbon/Ribbon_Parent.md), [UserInterfaceEvents.Parent](../UserInterfaceEvents/UserInterfaceEvents_Parent.md), [WebBrowserDockableWindow.Parent](WebBrowserDockableWindow_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add commands to the application menu](../../sample-programs/AddButtonToAppMenu_Sample.md) | Demonstrates adding command to the application menu. |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Dockable window](../../sample-programs/DockableWindows_Add_Sample.md) | This sample demonstrates creating a dockable window and adding a dialog into it. |
| [Print information about all available ribbons.](../../sample-programs/DumpRibbons_Sample.md) | This sample prints out all of the elements of the ribbons. This output is very useful when customizing the ribbon to be able to get the names of the various existing ribbons, tabs, and panels. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |