# RibbonPanels Object

## Description

The RibbonPanels collection object provides access to all existing panels within a ribbon tab and provides methods to create additional panels.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../RibbonPanels/RibbonPanels_Add.md) | Method that creates a new RibbonPanel within a ribbon tab. The newly created RibbonPanel is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RibbonPanels/RibbonPanels_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../RibbonPanels/RibbonPanels_Count.md) | Property that returns the number of items in this collection. |
| [Item](../RibbonPanels/RibbonPanels_Item.md) | Returns the specified RibbonPanel object from the collection. |
| [Type](../RibbonPanels/RibbonPanels_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[RibbonTab.RibbonPanels](../RibbonTab/RibbonTab_RibbonPanels.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |