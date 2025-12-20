# Ribbon Object

## Description

The Ribbon object represents the user interface containing a collection of tabs.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Active](../Ribbon/Ribbon_Active.md) | Property that returns whether this ribbon is currently being displayed. |
| [Application](../Ribbon/Ribbon_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [InternalName](../Ribbon/Ribbon_InternalName.md) | Property that returns the internal name of the ribbon. |
| [Parent](../Ribbon/Ribbon_Parent.md) | Property that returns the parent UserInterfaceManager object. |
| [QuickAccessControls](../Ribbon/Ribbon_QuickAccessControls.md) | Property that returns a CommandControls collection containing the controls in the Quick Access Toolbar (QAT). |
| [RibbonTabs](../Ribbon/Ribbon_RibbonTabs.md) | Property that returns the RibbonTabs collection object. |
| [Type](../Ribbon/Ribbon_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Environment.Ribbon](../Environment/Environment_Ribbon.md), [Ribbons.Item](../Ribbons/Ribbons_Item.md), [RibbonTab.Parent](../RibbonTab/RibbonTab_Parent.md)

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

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |