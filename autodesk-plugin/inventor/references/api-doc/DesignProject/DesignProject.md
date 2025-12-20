# DesignProject Object

## Description

The DesignProject object represents an Inventor project file (.ipj).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../DesignProject/DesignProject_Activate.md) | Method that activates the DesignProject. This requires all the documents to be closed in Inventor. |
| [GetCustomSection](../DesignProject/DesignProject_GetCustomSection.md) | Method that returns a custom section (in the form of an XML string) from the project file. |
| [GetIncludedCustomSection](../DesignProject/DesignProject_GetIncludedCustomSection.md) | Method that returns a custom section (in the form of an XML string) from the included project file. |
| [Remove](../DesignProject/DesignProject_Remove.md) | Method that removes the DesignProject from the list of available project files. This does not delete the .ipj file on disk. This method fails if the project is currently active. |
| [SetCustomSection](../DesignProject/DesignProject_SetCustomSection.md) | Method that adds or modifies a custom section (in the form of an XML string) in the project file. If a section with the given name is found, the section is replaced, else the section is added. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveAppearanceLibrary](../DesignProject/DesignProject_ActiveAppearanceLibrary.md) | Read-only property that returns the currently active appearance library. |
| [ActiveMaterialLibrary](../DesignProject/DesignProject_ActiveMaterialLibrary.md) | Read-only property that returns the currently active material library. |
| [AppearanceLibraries](../DesignProject/DesignProject_AppearanceLibraries.md) | Read-only property that returns the collection of appearance libraries associated with this project. |
| [Application](../DesignProject/DesignProject_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ContentCenterPath](../DesignProject/DesignProject_ContentCenterPath.md) | Read-write property that gets and sets the directory in which to look for the Content Center components. If set, this value overrides the corresponding application option. The ContentCenterPathOverridden property returns whether the path is overridden and provides the ability to clear the override. |
| [ContentCenterPathOverridden](../DesignProject/DesignProject_ContentCenterPathOverridden.md) | Gets and sets whether the content center path is overridden by this project. Setting the property to False clears the override and path in the application option is used. |
| [CreationTime](../DesignProject/DesignProject_CreationTime.md) | Gets and sets the creation time of the project file. |
| [DesignDataPath](../DesignProject/DesignProject_DesignDataPath.md) | Read-write property that gets and sets the directory in which to look for the Design Data such as styles. If set, this value overrides the corresponding application option. The DesignDataPathOverridden property returns whether the path is overridden and provides the ability to clear the override. |
| [DesignDataPathOverridden](../DesignProject/DesignProject_DesignDataPathOverridden.md) | Gets and sets whether the design data path is overridden by this project. Setting the property to False clears the override and path in the application option is used. |
| [FrequentlyUsedPaths](../DesignProject/DesignProject_FrequentlyUsedPaths.md) | Property that returns a ProjectPaths object that contains the list of frequently used paths and provides ability to add/remove paths. |
| [FullFileName](../DesignProject/DesignProject_FullFileName.md) | Property that returns the fully qualified file name for this design project. |
| [IncludedProject](../DesignProject/DesignProject_IncludedProject.md) | Read-write property that gets and sets the full file name of another project to include in this project. The search paths in the included file are included in the project. The project type of the included file overrides the setting in the project. The property can be set to a null string to indicate that there are no included projects. |
| [LibraryPaths](../DesignProject/DesignProject_LibraryPaths.md) | Property that returns a ProjectPaths object that contains the list of library paths and provides ability to add/remove paths. |
| [MaterialLibraries](../DesignProject/DesignProject_MaterialLibraries.md) | Read-only property that returns the collection of material libraries associated with this project. |
| [Name](../DesignProject/DesignProject_Name.md) | Gets and sets the name for this design project. |
| [OldVersionsToKeep](../DesignProject/DesignProject_OldVersionsToKeep.md) | Gets and sets the number of versions to store in the OldVersions folder for each file saved. The first time a file is saved. |
| [Owner](../DesignProject/DesignProject_Owner.md) | Gets and sets the string identifying the owner of the project. |
| [Parent](../DesignProject/DesignProject_Parent.md) | Property that returns the parent DesignProjectManager object. |
| [PresetsPath](../DesignProject/DesignProject_PresetsPath.md) | Gets and sets the directory in which to look for the Presets path. If set, this value overrides the corresponding directory. |
| [PresetsPathOverridden](../DesignProject/DesignProject_PresetsPathOverridden.md) | Gets and sets whether the presets path is overridden by this project. Setting the property to False clears the override and path in the application option is used. |
| [ProjectType](../DesignProject/DesignProject_ProjectType.md) | Read-write property that gets and sets the project type. Setting the type to shared or semi-isolated requires workgroup(s) to be specified. Setting the type to a Vault project requires a workspace to be specified but no workgroups or included project should be specified. |
| [ReleaseId](../DesignProject/DesignProject_ReleaseId.md) | Gets and sets version of the project. |
| [Shortcuts](../DesignProject/DesignProject_Shortcuts.md) | Gets and sets an array of strings specifying the shortcuts for the project. |
| [StylesLibraryAccess](../DesignProject/DesignProject_StylesLibraryAccess.md) | Gets/Sets the status of the styles library access for the Design Project. |
| [TemplatesPath](../DesignProject/DesignProject_TemplatesPath.md) | Read-write property that gets and sets the directory in which to look for the template files. If set, this value overrides the corresponding application option. The TemplatesPathOverridden property returns whether the path is overridden and provides the ability to clear the override. |
| [TemplatesPathOverridden](../DesignProject/DesignProject_TemplatesPathOverridden.md) | Gets and sets whether the templates path is overridden by this project. Setting the property to False clears the override and path in the application option is used. |
| [Type](../DesignProject/DesignProject_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UsingUniqueFileNames](../DesignProject/DesignProject_UsingUniqueFileNames.md) | Gets and sets whether duplicate file names are used in the project. |
| [VaultName](../DesignProject/DesignProject_VaultName.md) | Gets and sets the vault name. Applicable only if the ProjectType is set to kVaultMode. |
| [VaultPublishPath](../DesignProject/DesignProject_VaultPublishPath.md) | Gets and sets the publish folder for Vault. Applicable only if the ProjectType is set to kVaultMode. |
| [VaultServer](../DesignProject/DesignProject_VaultServer.md) | Gets and sets the vault server. Applicable only if the ProjectType is set to kVaultMode. |
| [VaultVirtualPath](../DesignProject/DesignProject_VaultVirtualPath.md) | Gets and sets the virtual folder for Vault. Applicable only if the ProjectType is set to kVaultMode. |
| [WorkgroupPaths](../DesignProject/DesignProject_WorkgroupPaths.md) | Property that returns a ProjectPaths object that contains the list of workgroup paths and provides ability to add/remove paths. |
| [WorkspacePath](../DesignProject/DesignProject_WorkspacePath.md) | Gets and sets the workspace folder for the project. |

## Accessed From

[ContentCenterConfiguration.Parent](ContentCenterConfiguration_Parent.md), [DesignProjectManager.ActiveDesignProject](../DesignProjectManager/DesignProjectManager_ActiveDesignProject.md), [DesignProjects.Add](../DesignProjects/DesignProjects_Add.md), [DesignProjects.AddExisting](../DesignProjects/DesignProjects_AddExisting.md), [DesignProjects.Item](../DesignProjects/DesignProjects_Item.md), [DesignProjects.ItemByName](../DesignProjects/DesignProjects_ItemByName.md), [IntentConfiguration.Parent](IntentConfiguration_Parent.md), [ProjectAssetLibrary.Parent](../ProjectAssetLibrary/ProjectAssetLibrary_Parent.md), [ProjectPath.Parent](../ProjectPath/ProjectPath_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Set active project](../../sample-programs/ProjectActivate_Sample.md) | The following sample demonstrates the activation of an Inventor project. |

## Version

Introduced in version 7

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |