# Environments.Add Method

Parent Object: [Environments](../Environments/Environments.md)

## Description

Method that creates a new Environment object.

## Syntax

Environments.**Add**( ***DisplayName*** As String, ***InternalName*** As String, [***ClientId***] As Variant, [***StandardIcon***] As Variant, [***LargeIcon***] As Variant ) As [Environment](../Environment/Environment.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DisplayName | String | Input string that defines the display name of the environment. This is the name that is displayed to the user and should be localized for different locales. |
| InternalName | String | Input string that defines the name of the environment. This is the internal name and is not displayed to the user. The name must be unique with respect to all other environments and is typically a GUID. The name should remain constant in all locales to it can be used to find a specific environment. |
| ClientId | Variant | Optional input string that uniquely identifies the client. Ignored for VBA clients, but Addins should supply the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". If supplied, this string is used at Inventor start up time to determine whether the AddIn that created this environment has since been uninstalled. If so, the environment is deleted. If a ClientId is supplied, it must be the CLSID of an Add-in, else the method returns a failure. |
| StandardIcon | Variant | Optional input Picture object that specifies the standard size icon to use for the environment. A standard size icon is 16 pixels wide and 16 pixels high. All icons use 16 colors. If not supplied the icon from the source environment will be used.   This is an optional argument whose default value is null. |
| LargeIcon | Variant | Optional input Picture object that specifies the large size icon to use for the environment. A large size icon is 24 pixels wide and 24 pixels high. All icons use 16 colors. If not supplied and a standard size icon is supplied a large icon will be automatically created by scaling the standard size icon. Because scaling a bitmap does not necessarily create a good image, it is recommended that you create and supply a large bitmap.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add parallel environment with contextual tabs](../../sample-programs/CreateParallelEnvironment_Sample.md) | The following sample demonstrates the use of parallel environments and contextual ribbon tabs. |
| [Creation of an override environment for a document](../../sample-programs/EnvironmentManager_OverrideEnvironment_Sample.md) | A new ribbon tab is created and associated with the override environment. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |