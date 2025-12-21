# RibbonTab Object

## Description

A RibbonTab object represents a tab within a ribbon.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RibbonTab/RibbonTab_Delete.md) | Method that deletes the RibbonTab. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Active](../RibbonTab/RibbonTab_Active.md) | Gets and sets whether this tab is currently active. Setting this property returns an error if the parent ribbon is not active. |
| [Application](../RibbonTab/RibbonTab_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ClientId](../RibbonTab/RibbonTab_ClientId.md) | Property that returns the string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |
| [Contextual](../RibbonTab/RibbonTab_Contextual.md) | Gets and sets whether this tab is contextual. |
| [DisplayName](../RibbonTab/RibbonTab_DisplayName.md) | Property that returns the display name of the ribbon tab. |
| [InternalName](../RibbonTab/RibbonTab_InternalName.md) | Property that returns the unique internal name of the ribbon tab. |
| [KeyTip](../RibbonTab/RibbonTab_KeyTip.md) | Gets and sets the keyboard access key for the tab. |
| [Parent](../RibbonTab/RibbonTab_Parent.md) | Property that returns the parent Ribbon object. |
| [RibbonPanels](../RibbonTab/RibbonTab_RibbonPanels.md) | Property that returns the RibbonPanels collection object. |
| [Type](../RibbonTab/RibbonTab_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../RibbonTab/RibbonTab_Visible.md) | Gets and sets whether the ribbon tab is currently visible in the ribbon. Note that this property applies only when the parent ribbon is active. |

## Accessed From

[RibbonPanel.Parent](../RibbonPanel/RibbonPanel_Parent.md), [RibbonTabs.Add](../RibbonTabs/RibbonTabs_Add.md), [RibbonTabs.Item](../RibbonTabs/RibbonTabs_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |

## Version

Introduced in version 2010
