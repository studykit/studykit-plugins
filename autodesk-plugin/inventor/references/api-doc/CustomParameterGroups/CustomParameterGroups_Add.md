# CustomParameterGroups.Add Method

Parent Object: [CustomParameterGroups](../CustomParameterGroups/CustomParameterGroups.md)

## Description

Method that adds a custom parameter group.

## Syntax

CustomParameterGroups.**Add**( ***DisplayName*** As String, ***InternalName*** As String, [***ClientId***] As String ) As [CustomParameterGroup](../CustomParameterGroup/CustomParameterGroup.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DisplayName | String | Input string that defines the display name of the custom group. This is the name that is displayed to the user and should be localized for different locales. |
| InternalName | String | Input string that defines the name of the custom group. This is the internal name and is not displayed to the user. The name must be unique with respect to all other groups. The name should remain constant in all locales to it can be used to find a specific group. |
| ClientId | String | Optional input string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating a new parameter group](../../sample-programs/CustomParameterGroup_Add_Sample.md) | This sample demonstrates the creation of model, reference and user parameters and copying these parameters to a newly created group. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |