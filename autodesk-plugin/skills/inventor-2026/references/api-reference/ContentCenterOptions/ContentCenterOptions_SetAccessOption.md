# ContentCenterOptions.SetAccessOption Method

Parent Object: [ContentCenterOptions](../ContentCenterOptions/ContentCenterOptions.md)

## Description

Method that sets the access option for content center (Inventor Desktop or Vault/Productstream).

## Syntax

ContentCenterOptions.**SetAccessOption**( ***AccessOption*** As [ContentCenterAccessOptionEnum](../ContentCenterAccessOptionEnum.md), [***LibrariesLocation***] As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AccessOption | [ContentCenterAccessOptionEnum](../ContentCenterAccessOptionEnum.md) | Input ContentCenterAccessOptionEnum value that specifies the access option for content center. This can either be kInventorDesktopAccess or kVaultOrProductstreamServerAccess. If kInventorDesktopAccess is input, the LibrariesLocation argument must be specified. |
| LibrariesLocation | String | Optional input String that specifies the location of the libraries if the access option is kInventorDesktopAccess. The argument must be specified for kInventorDesktopAccess, and can be ignored for kVaultOrProductstreamServerAccess. |

## Version

Introduced in version 2010
