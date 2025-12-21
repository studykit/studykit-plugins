# RibbonPanel Object

## Description

A RibbonPanel object represents a panel within a ribbon tab.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RibbonPanel/RibbonPanel_Delete.md) | Method that deletes the RibbonPanel. |
| [Move](../RibbonPanel/RibbonPanel_Move.md) | Method that moves the ribbon panel. If the panel is docked, calling this method automatically undocks the panel and honors the input values. |
| [Reposition](../RibbonPanel/RibbonPanel_Reposition.md) | Method that moves the RibbonPanel to a new location within the ribbon tab. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RibbonPanel/RibbonPanel_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ClientId](../RibbonPanel/RibbonPanel_ClientId.md) | Property that returns the string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |
| [CommandControls](../RibbonPanel/RibbonPanel_CommandControls.md) | Property that returns the CommandControls collection object that provides access to all the visible controls within the panel. |
| [DisplayName](../RibbonPanel/RibbonPanel_DisplayName.md) | Property that returns the display name of the ribbon panel. |
| [Docked](../RibbonPanel/RibbonPanel_Docked.md) | Gets sets whether the ribbon panel docked within the ribbon. |
| [InternalName](../RibbonPanel/RibbonPanel_InternalName.md) | Property that returns the unique internal name of the ribbon panel. |
| [Parent](../RibbonPanel/RibbonPanel_Parent.md) | Property that returns the parent RibbonTab object. |
| [SlideoutControls](../RibbonPanel/RibbonPanel_SlideoutControls.md) | Property that returns the CommandControls collection object that provides access to all controls in the slideout section of the panel. ![](../images/RibbonPanel_SlideOutControls.png) |
| [SlideOutKeyTip](../RibbonPanel/RibbonPanel_SlideOutKeyTip.md) | Gets and sets the keyboard access key for the slideout controls within the panel. |
| [Type](../RibbonPanel/RibbonPanel_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../RibbonPanel/RibbonPanel_Visible.md) | Gets and sets whether the ribbon panel is currently visible in the ribbon. Note that this property applies only when the parent ribbon tab and the ribbon within which the tab lives are currently active. |

## Accessed From

[RibbonPanels.Add](../RibbonPanels/RibbonPanels_Add.md), [RibbonPanels.Item](../RibbonPanels/RibbonPanels_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Print information about all available ribbons.](../../sample-programs/DumpRibbons_Sample.md) | This sample prints out all of the elements of the ribbons. This output is very useful when customizing the ribbon to be able to get the names of the various existing ribbons, tabs, and panels. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |

## Version

Introduced in version 2010
