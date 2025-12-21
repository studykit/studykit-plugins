# ProjectPaths Object

## Description

The ProjectPaths collection object provides access to a list of folder paths and provides ability to add/remove paths.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ProjectPaths/ProjectPaths_Add.md) | Method that adds a folder path after the target index and returns the newly created ProjectPath object. |
| [AddFromFile](../ProjectPaths/ProjectPaths_AddFromFile.md) | Method that adds folder paths from an existing project (.ipj) \file. |
| [Clear](../ProjectPaths/ProjectPaths_Clear.md) | Method that deletes all the paths in the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProjectPaths/ProjectPaths_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../ProjectPaths/ProjectPaths_Count.md) | Property that returns the number of items in the collection. |
| [Item](../ProjectPaths/ProjectPaths_Item.md) | Returns the specified ProjectPath object from the collection. |
| [Type](../ProjectPaths/ProjectPaths_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DesignProject.FrequentlyUsedPaths](../DesignProject/DesignProject_FrequentlyUsedPaths.md), [DesignProject.LibraryPaths](../DesignProject/DesignProject_LibraryPaths.md), [DesignProject.WorkgroupPaths](../DesignProject/DesignProject_WorkgroupPaths.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Query and create library paths](../../sample-programs/ProjectLibraryPaths_Sample.md) | The following sample demonstrates querying existing library paths associated with a project and adding a new library path. |

## Version

Introduced in version 2011
