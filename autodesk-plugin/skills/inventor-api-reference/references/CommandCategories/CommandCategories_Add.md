# CommandCategories.Add Method

Parent Object: [CommandCategories](../CommandCategories/CommandCategories.md)

## Description

Method that adds a .

## Syntax

CommandCategories.**Add**( ***DisplayName*** As String, ***InternalName*** As String, [***ClientId***] As Variant ) As [CommandCategory](../CommandCategory/CommandCategory.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DisplayName | String | Input string that defines the display name of the command category. This is the name that is displayed to the user and should be localized for different locales. |
| InternalName | String | Input string that defines the name of the command category. This is the internal name and is not displayed to the user. The name must be unique with respect to all other command categories. The name should remain constant in all locales to it can be used to find a specific command category. |
| ClientId | Variant | Input string that uniquely identifies the client. Suggestions are the 'ProgID' of the Add-In creating the resource or its CLSID in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}", although any unique string is valid. If you do not use a CLSID or a ProgID, it is recommended that you add your application name to the ClientId to help eliminate naming conflicts. |

## Version

Introduced in version 9
