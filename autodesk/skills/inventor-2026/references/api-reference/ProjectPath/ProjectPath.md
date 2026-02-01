# ProjectPath Object

## Description

The ProjectPath object represents a folder path for a library, workspace or a workgroup.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ProjectPath/ProjectPath_Delete.md) | Method that deletes this path from the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProjectPath/ProjectPath_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Name](../ProjectPath/ProjectPath_Name.md) | Read-write property that gets and sets the name of the folder path. |
| [Parent](../ProjectPath/ProjectPath_Parent.md) | Property that returns the parent DesignProject object. |
| [Path](../ProjectPath/ProjectPath_Path.md) | Read-write property that gets and sets the folder path associated with this object. |
| [Type](../ProjectPath/ProjectPath_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ProjectPaths.Add](../ProjectPaths/ProjectPaths_Add.md), [ProjectPaths.Item](../ProjectPaths/ProjectPaths_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Query and create library paths](../../sample-programs/ProjectLibraryPaths_Sample.md) | The following sample demonstrates querying existing library paths associated with a project and adding a new library path. |

## Version

Introduced in version 2011
