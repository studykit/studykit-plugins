# ControlDefinitions.AddMacroControlDefinition Method

Parent Object: [ControlDefinitions](../ControlDefinitions/ControlDefinitions.md)

## Description

Method that creates a new MacroControlDefinition object. The MacroControlDefinition object is used to define the information associated with a button that can be used to execute an Inventor VBA macro, insert an iPart, insert an iFeature or execute an EXE.

## Syntax

ControlDefinitions.**AddMacroControlDefinition**( ***MacroOrProgram*** As String ) As [MacroControlDefinition](../MacroControlDefinition/MacroControlDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| MacroOrProgram | String | Input String that defines the VBA macro to run, the external file to insert or EXE program to run. A VBA macro must be a Public Sub defined in a standard code module of the Application VBA project. The Sub cannot have any input arguments. The Sub is specified using 'Module.SubName' format. For example the Sub MovePart in a module named AsmTools would be specified by 'AsmTools.MovePart'. If a filename with a .ipt extension is supplied it is assumed to be an iPart. The filename must be a full filename. If an external EXE is specified, this argument must be the full path to the EXE. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |