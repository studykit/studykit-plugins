# EnvironmentList Object

## Description

The EnvironmentList object defines a list of environments that are displayed to the user in various contexts. For more information, refer to the [Environments overviews](Environments_Overview.md).

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../EnvironmentList/EnvironmentList_Add.md) | Method that adds an Environment object to the list. The method returns an error if a built-in Environment is supplied. |
| [Remove](../EnvironmentList/EnvironmentList_Remove.md) | Method that removes the specified Environment from the list. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EnvironmentList/EnvironmentList_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../EnvironmentList/EnvironmentList_Count.md) | Property that returns the number of environments currently in the list. |
| [Item](../EnvironmentList/EnvironmentList_Item.md) | Returns the specified Environment object from the list. |
| [Type](../EnvironmentList/EnvironmentList_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[UserInterfaceManager.ParallelEnvironments](../UserInterfaceManager/UserInterfaceManager_ParallelEnvironments.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |

## Version

Introduced in version 10
