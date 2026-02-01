# Ribbons Object

## Description

The Ribbons collection object provides access to all existing ribbons in Inventor.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Ribbons/Ribbons_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../Ribbons/Ribbons_Count.md) | Property that returns the number of items in this collection. |
| [Item](../Ribbons/Ribbons_Item.md) | Returns the specified Ribbon object from the collection. |
| [Type](../Ribbons/Ribbons_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[UserInterfaceManager.Ribbons](../UserInterfaceManager/UserInterfaceManager_Ribbons.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |

## Version

Introduced in version 2010
