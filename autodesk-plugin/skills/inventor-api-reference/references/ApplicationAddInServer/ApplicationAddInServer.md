# ApplicationAddInServer Object

## Description

Object required to be supported by Server to qualify as an Autodesk Inventor AddIn.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../ApplicationAddInServer/ApplicationAddInServer_Activate.md) | Invoked by Autodesk Inventor after creating the AddIn. AddIn should initialize within this call. |
| [Deactivate](../ApplicationAddInServer/ApplicationAddInServer_Deactivate.md) | Invoked by Autodesk Inventor to shut down the AddIn. AddIn should complete shutdown within this call. |
| [ExecuteCommand](../ApplicationAddInServer/ApplicationAddInServer_ExecuteCommand.md) | Invoked by Autodesk Inventor in response to user requesting the execution of an AddIn-supplied command. AddIn must perform the command within this call. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Automation](../ApplicationAddInServer/ApplicationAddInServer_Automation.md) | Gets the IUnknown of the object implemented inside the AddIn that supports AddIn-specific API. |

## Derived Classes

[TranslatorAddInServer](../TranslatorAddInServer/TranslatorAddInServer.md)

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |