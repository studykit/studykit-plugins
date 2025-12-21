# TranslatorAddInServer.ExecuteCommand Method

Parent Object: [TranslatorAddInServer](../TranslatorAddInServer/TranslatorAddInServer.md)

## Description

Invoked by Autodesk Inventor in response to user requesting the execution of an AddIn-supplied command. AddIn must perform the command within this call.

## Syntax

TranslatorAddInServer.**ExecuteCommand**( ***CommandID*** As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CommandID | Long | Input Long that specifies the command to execute. |

## Version

Introduced in version 4
