# CommandControls Object

## Description

The CommandControls collection object provides access to a collection of user interface controls and provides methods to create additional controls.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddButton](../CommandControls/CommandControls_AddButton.md) | Method that creates a new button CommandControl object. An example of this type of control is the 'Extrude' feature command button. |
| [AddButtonPopup](../CommandControls/CommandControls_AddButtonPopup.md) | Method that creates a new popup CommandControl object. An example of this type of control is the 'Display Mode' drop down (Shaded, Hidden Edge, Wireframe) available on the 'View' tab of the ribbon in parts and assemblies. |
| [AddComboBox](../CommandControls/CommandControls_AddComboBox.md) | Method that creates a new combo-box CommandControl object. |
| [AddCopy](../CommandControls/CommandControls_AddCopy.md) | Method that creates a copy of an existing CommandControl object as a child control of the current CommandControl. This can be used to copy controls between ribbon panels. |
| [AddGallery](../CommandControls/CommandControls_AddGallery.md) | Method that creates a new gallery CommandControl object. An example of this type of control is the gallery control available in the Symbols panel of the Annotate tab in drawings. |
| [AddMacro](../CommandControls/CommandControls_AddMacro.md) | Method that creates a new macro CommandControl object. |
| [AddPopup](../CommandControls/CommandControls_AddPopup.md) | Method that creates a new popup CommandControl object. An example of this type of control is the 'Switch' control available in the Windows panel of the View tab. |
| [AddSeparator](../CommandControls/CommandControls_AddSeparator.md) | Method that creates a new separator CommandControl object. |
| [AddSplitButton](../CommandControls/CommandControls_AddSplitButton.md) | Method that creates a new split button CommandControl object. An example of this type of control is the 'New File' split button drop down available in the Quick Access Toolbar. |
| [AddSplitButtonMRU](../CommandControls/CommandControls_AddSplitButtonMRU.md) | Method that creates a new split button MRU (Most Recently Used) CommandControl object. An example of this type of control is the 'Circle' drop down in the Sketch tab of the ribbon. |
| [AddTogglePopup](../CommandControls/CommandControls_AddTogglePopup.md) | Method that creates a new toggle popup CommandControl object. An example of this type of control is the 'Object Visibility' control available in the Visibility panel of the Views tab. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CommandControls/CommandControls_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../CommandControls/CommandControls_Count.md) | Property that returns the number of items in this collection. |
| [Item](../CommandControls/CommandControls_Item.md) | Returns the specified CommandControl object from the collection. |
| [Type](../CommandControls/CommandControls_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CommandControl.ChildControls](../CommandControl/CommandControl_ChildControls.md), [Ribbon.QuickAccessControls](../Ribbon/Ribbon_QuickAccessControls.md), [RibbonPanel.CommandControls](../RibbonPanel/RibbonPanel_CommandControls.md), [RibbonPanel.SlideoutControls](../RibbonPanel/RibbonPanel_SlideoutControls.md), [UserInterfaceManager.FileBrowserControls](../UserInterfaceManager/UserInterfaceManager_FileBrowserControls.md), [UserInterfaceManager.HelpControls](../UserInterfaceManager/UserInterfaceManager_HelpControls.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add commands to the application menu](../../sample-programs/AddButtonToAppMenu_Sample.md) | Demonstrates adding command to the application menu. |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Print information about all available ribbons.](../../sample-programs/DumpRibbons_Sample.md) | This sample prints out all of the elements of the ribbons. This output is very useful when customizing the ribbon to be able to get the names of the various existing ribbons, tabs, and panels. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |

## Version

Introduced in version 2010
