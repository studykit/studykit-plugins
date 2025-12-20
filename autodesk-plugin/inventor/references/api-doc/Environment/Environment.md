# Environment Object

## Description

The Environment object represents any Autodesk Inventor environment. Example environments are Part, Assembly, Sketch, etc. The Environment represents the current state of an environment. See the [UI customization](RibbonUI_Overview.md) and [Environments overviews](Environments_Overview.md) for more information.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../Environment/Environment_Delete.md) | Method that deletes the environment. This method will fail for built-in environments. |
| [GetRadialMarkingMenu](../Environment/Environment_GetRadialMarkingMenu.md) | Returns the RadialMarkingMenu object that can be used to query and set the commands available in the radial menu for the input object type. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AdditionalVisibleRibbonTabs](../Environment/Environment_AdditionalVisibleRibbonTabs.md) | Gets and sets an array of strings containing the internal names of ribbon tabs that should be displayed in this environment. These are in addition to the tabs displayed as a result of setting the InheritAllRibbonTabs property to True. |
| [Application](../Environment/Environment_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BuiltIn](../Environment/Environment_BuiltIn.md) | Property that specifies if the Environment a standard Autodesk Inventor Environment or if it has been added by a client. Built-in environments have restrictions in the edits that can be performed. For example, build-in environments cannot be deleted. For more information, see the Environments overview. |
| [ClientId](../Environment/Environment_ClientId.md) | Property that returns the string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |
| [DefaultRibbonTab](../Environment/Environment_DefaultRibbonTab.md) | Gets and sets the internal name of the ribbon tab that should be displayed when this environment is activated. |
| [DisabledCommandList](../Environment/Environment_DisabledCommandList.md) | Property that returns the DisabledCommandList object. This object allows the environment to disable commands when this environment is active. This list contains commands that are disabled in addition to those specified by the DisabledCommandTypes property. |
| [DisabledCommandTypes](../Environment/Environment_DisabledCommandTypes.md) | Gets list of disabled command types for the Environment. |
| [DisplayName](../Environment/Environment_DisplayName.md) | Display Name of the Environment. |
| [ExitDisplayName](../Environment/Environment_ExitDisplayName.md) | Gets and sets the exit display name of the environment, to be used on the Finish button. As default this will be the same as the DisplayName. This is the name displayed to the user and should be localized for the current locale. |
| [InheritAllRibbonTabs](../Environment/Environment_InheritAllRibbonTabs.md) | Gets and sets whether this environment should inherit all ribbon tabs from the 'base' environment. This property applies only to custom environments. If set to True, all visible tabs in the base environment are displayed in this environment. |
| [InternalName](../Environment/Environment_InternalName.md) | Property that indicates the name of the environment. |
| [LargeIcon](../Environment/Environment_LargeIcon.md) | Gets and sets the LargeIcon for the Environment. |
| [Parent](../Environment/Environment_Parent.md) | Property that returns the parent of the environment. |
| [PreserveWhenSwitchModelState](../Environment/Environment_PreserveWhenSwitchModelState.md) | Gets and sets whether the environment status would be preserved when switch model state in an assembly. This would make sure the environment to be preserved when switch between substitute model state and other model state in an assembly.For built-in environmen. |
| [RadialMarkingMenus](../Environment/Environment_RadialMarkingMenus.md) | Returns the RadialMarkingMenus object that can be used to query and set the selection based radial menu. |
| [Ribbon](../Environment/Environment_Ribbon.md) | Property that returns the Ribbon object associated with this environment. This property returns Nothing when the environment is initially created and not yet applied as an override or a parallel environment. |
| [StandardIcon](../Environment/Environment_StandardIcon.md) | Gets and sets the StandardIcon for the Environment. |
| [Type](../Environment/Environment_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[EnvironmentList.Item](../EnvironmentList/EnvironmentList_Item.md), [EnvironmentManager.BaseEnvironment](../EnvironmentManager/EnvironmentManager_BaseEnvironment.md), [EnvironmentManager.EditObjectEnvironment](../EnvironmentManager/EnvironmentManager_EditObjectEnvironment.md), [EnvironmentManager.GetCurrentEnvironment](../EnvironmentManager/EnvironmentManager_GetCurrentEnvironment.md), [EnvironmentManager.OverrideEnvironment](../EnvironmentManager/EnvironmentManager_OverrideEnvironment.md), [Environments.Add](../Environments/Environments_Add.md), [Environments.Item](../Environments/Environments_Item.md), [PanelBar.Parent](PanelBar_Parent.md), [UserInterfaceManager.ActiveEnvironment](../UserInterfaceManager/UserInterfaceManager_ActiveEnvironment.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |