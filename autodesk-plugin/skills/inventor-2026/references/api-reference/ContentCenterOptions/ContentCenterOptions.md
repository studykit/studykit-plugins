# ContentCenterOptions Object

## Description

The ContentCenterOptions object provides access to properties that provide read and write access of the content center related application options.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetAccessOption](../ContentCenterOptions/ContentCenterOptions_GetAccessOption.md) | Method that gets the access option for content center (Inventor Desktop or Vault/Productstream). |
| [SetAccessOption](../ContentCenterOptions/ContentCenterOptions_SetAccessOption.md) | Method that sets the access option for content center (Inventor Desktop or Vault/Productstream). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ContentCenterOptions/ContentCenterOptions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CheckFamiliesUpdates](../ContentCenterOptions/ContentCenterOptions_CheckFamiliesUpdates.md) | Gets/sets how to handle linked families - check/do not check for parent version. |
| [CustomFamilyAsStandard](../ContentCenterOptions/ContentCenterOptions_CustomFamilyAsStandard.md) | Gets/sets whether to place Family with custom's columns As Standard or As Custom. |
| [RefreshOutOfDateStandardParts](../ContentCenterOptions/ContentCenterOptions_RefreshOutOfDateStandardParts.md) | Gets/sets whether to automatically refresh out of date standard parts during placement. |
| [Type](../ContentCenterOptions/ContentCenterOptions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.ContentCenterOptions](../Application/Application_ContentCenterOptions.md), [InventorServer.ContentCenterOptions](InventorServer_ContentCenterOptions.md), [InventorServerObject.ContentCenterOptions](InventorServerObject_ContentCenterOptions.md)

## Version

Introduced in version 2010
