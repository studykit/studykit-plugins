# ProjectAssetLibrary Object

## Description

The ProjectAssetLibrary object represents a reference in this project to a material or appearance library.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../ProjectAssetLibrary/ProjectAssetLibrary_Activate.md) | Method that activates this material or appearance library.  The user can override this and specify another library as the currently active library using the check boxes at the bottom of the material drop-down, as shown below, which will not change the project settings. ![](../Images/ActiveAssetLibrary.png) |
| [Delete](../ProjectAssetLibrary/ProjectAssetLibrary_Delete.md) | Method that deletes this library reference from the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ProjectAssetLibrary/ProjectAssetLibrary_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [LibraryFilename](../ProjectAssetLibrary/ProjectAssetLibrary_LibraryFilename.md) | Read-only property that returns the full filename of the library file. |
| [Name](../ProjectAssetLibrary/ProjectAssetLibrary_Name.md) | Read-only property that returns the name of the library. This is the name displayed in the Projects dialog. |
| [Parent](../ProjectAssetLibrary/ProjectAssetLibrary_Parent.md) | Read-only property that returns the parent DesignProject object. |
| [Type](../ProjectAssetLibrary/ProjectAssetLibrary_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DesignProject.ActiveAppearanceLibrary](../DesignProject/DesignProject_ActiveAppearanceLibrary.md), [DesignProject.ActiveMaterialLibrary](../DesignProject/DesignProject_ActiveMaterialLibrary.md), [ProjectAssetLibraries.Add](../ProjectAssetLibraries/ProjectAssetLibraries_Add.md), [ProjectAssetLibraries.Item](../ProjectAssetLibraries/ProjectAssetLibraries_Item.md)

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |