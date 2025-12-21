# RibbonTabs Object

## Description

The RibbonTabs collection object provides access to all existing tabs within a ribbon and provides methods to create additional tabs.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../RibbonTabs/RibbonTabs_Add.md) | Method that creates a new RibbonTab within a ribbon. The newly created RibbonTab is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RibbonTabs/RibbonTabs_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../RibbonTabs/RibbonTabs_Count.md) | Property that returns the number of items in this collection. |
| [Item](../RibbonTabs/RibbonTabs_Item.md) | Returns the specified RibbonTab object from the collection. |
| [Type](../RibbonTabs/RibbonTabs_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Ribbon.RibbonTabs](../Ribbon/Ribbon_RibbonTabs.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |

## Version

Introduced in version 2010
