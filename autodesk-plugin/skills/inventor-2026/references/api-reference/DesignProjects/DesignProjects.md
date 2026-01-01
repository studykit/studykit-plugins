# DesignProjects Object

## Description

The DesignProjects collection object provides access to all the existing projects and provides methods to create additional projects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../DesignProjects/DesignProjects_Add.md) | Method that creates a new DesignProject. The newly created DesignProject is returned. |
| [AddExisting](../DesignProjects/DesignProjects_AddExisting.md) | Method that adds an existing project file to the list of project files. This is equivalent of browsing to a specific ipj file on disk and choosing it in the Projects editor dialog. If the design project is already in the collection, the corresponding DesignProject object is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DesignProjects/DesignProjects_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../DesignProjects/DesignProjects_Count.md) | Property that returns the number of items in the collection. |
| [Item](../DesignProjects/DesignProjects_Item.md) | Returns the specified DesignProject object from the collection. |
| [ItemByName](../DesignProjects/DesignProjects_ItemByName.md) | Returns the specified DesignProject object from the collection. |
| [Type](../DesignProjects/DesignProjects_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DesignProjectManager.DesignProjects](../DesignProjectManager/DesignProjectManager_DesignProjects.md)

## Version

Introduced in version 2011
