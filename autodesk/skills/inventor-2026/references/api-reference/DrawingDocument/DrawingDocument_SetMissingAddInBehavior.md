# DrawingDocument.SetMissingAddInBehavior Method

Parent Object: [DrawingDocument](../DrawingDocument/DrawingDocument.md)

## Description

Method that sets the commands to be disabled when a particular AddIn is absent.

## Syntax

DrawingDocument.**SetMissingAddInBehavior**( ***ClientId*** As String, ***DisabledCommandTypesEnum*** As [CommandTypesEnum](../CommandTypesEnum.md), [***DisabledCommands***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Specifies the ClassId of the AddIn. When the AddIn corresponding to this ClientId is absent (unloaded or uninstalled), the commands specified are disabled. |
| DisabledCommandTypesEnum | [CommandTypesEnum](../CommandTypesEnum.md) | CommandTypesEnum that specifies the classifications of the commands to be disabled. |
| DisabledCommands | Variant | Optional input ObjectCollection that specifies the commands to be disabled. The ObjectCollection must contain only ControlDefinition objects. |

## Version

Introduced in version 11
