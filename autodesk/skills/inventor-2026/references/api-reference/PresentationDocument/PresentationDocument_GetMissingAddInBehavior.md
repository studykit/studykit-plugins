# PresentationDocument.GetMissingAddInBehavior Method

Parent Object: [PresentationDocument](../PresentationDocument/PresentationDocument.md)

## Description

Method that gets the commands disabled when a particular AddIn is absent.

## Syntax

PresentationDocument.**GetMissingAddInBehavior**( ***ClientId*** As String, ***DisabledCommandTypesEnum*** As [CommandTypesEnum](../CommandTypesEnum.md), ***DisabledCommands*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Specifies the ClassId of the AddIn. When the AddIn corresponding to this ClientId is absent (unloaded or uninstalled), the commands specified are disabled. |
| DisabledCommandTypesEnum | [CommandTypesEnum](../CommandTypesEnum.md) | CommandTypesEnum that specifies the classifications of the commands disabled. |
| DisabledCommands | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | ObjectCollection that specifies the commands disabled. |

## Version

Introduced in version 11
