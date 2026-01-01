# TranslatorAddInServer.Activate Method

Parent Object: [TranslatorAddInServer](../TranslatorAddInServer/TranslatorAddInServer.md)

## Description

Invoked by Autodesk Inventor after creating the AddIn. AddIn should initialize within this call.

## Syntax

TranslatorAddInServer.**Activate**( ***AddInSiteObject*** As [ApplicationAddInSite](../ApplicationAddInSite/ApplicationAddInSite.md), ***FirstTime*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AddInSiteObject | [ApplicationAddInSite](../ApplicationAddInSite/ApplicationAddInSite.md) | Input argument that specifies the object, which provides access to the Autodesk Inventor Application object. |
| FirstTime | Boolean | The FirstTime flag, if True, indicates to the Addin that this is the first time it is being loaded and to take some specific action. It does not take these actions when this flag is False. Typically, when the flag is True, the AddIn proceeds to create all of the objects under the UserInterfaceManager that it needs - Environments, Ribbons and Controls. These objects are persistent, but if this is the first time the Addin is loaded, they need to be created from scratch. When the FirstTime flag is False, meaning the Addin has already been loaded, it only needs to create the objects under the CommandManager - CommandCategories and ControlDefinitions. |

## Version

Introduced in version 4
