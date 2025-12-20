# DesignProject.GetIncludedCustomSection Method

Parent Object: [DesignProject](../DesignProject/DesignProject.md)

## Description

Method that returns a custom section (in the form of an XML string) from the included project file.

## Syntax

DesignProject.**GetIncludedCustomSection**( ***Name*** As String ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that specifies name of the custom section in the included project file. If the section with the specified name is not found or there is no included project, a null string is returned. The following strings can be used to retrieve some of the built-in sections: 'ContentCenterConfig', 'VaultOptions', and 'AutodeskIntent'. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |