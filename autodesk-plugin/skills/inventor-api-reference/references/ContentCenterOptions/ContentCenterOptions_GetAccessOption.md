# ContentCenterOptions.GetAccessOption Method

Parent Object: [ContentCenterOptions](../ContentCenterOptions/ContentCenterOptions.md)

## Description

Method that gets the access option for content center (Inventor Desktop or Vault/Productstream).

## Syntax

ContentCenterOptions.**GetAccessOption**( ***AccessOption*** As [ContentCenterAccessOptionEnum](../ContentCenterAccessOptionEnum.md), ***LibrariesLocation*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AccessOption | [ContentCenterAccessOptionEnum](../ContentCenterAccessOptionEnum.md) | Output ContentCenterAccessOptionEnum value that returns the access option for content center. This can either be kInventorDesktopAccess or kVaultOrProductstreamServerAccess. If kInventorDesktopAccess is returned, the LibrariesLocation argument returns the location of the libraries. |
| LibrariesLocation | String | Output String that returns the location of the libraries if the access option is kInventorDesktopAccess. The argument returns a null string if the access option is kVaultOrProductstreamServerAccess. |

## Version

Introduced in version 2010
