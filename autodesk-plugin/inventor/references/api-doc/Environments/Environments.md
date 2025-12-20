# Environments Object

## Description

The Environments collection object provides access to all of the existing objects, and allows creation of new ones. See the [UI customization](RibbonUI_Overview.md) and [Environments overviews](Environments_Overview.md) for more information.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../Environments/Environments_Add.md) | Method that creates a new Environment object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Environments/Environments_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../Environments/Environments_Count.md) | Property that returns the number of Environments in the collection. |
| [Item](../Environments/Environments_Item.md) | Returns the specified Environment object from the collection. |
| [Type](../Environments/Environments_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[UserInterfaceManager.Environments](../UserInterfaceManager/UserInterfaceManager_Environments.md)

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