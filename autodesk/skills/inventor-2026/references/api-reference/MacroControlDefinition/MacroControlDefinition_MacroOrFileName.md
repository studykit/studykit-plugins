# MacroControlDefinition.MacroOrFileName Property

Parent Object: [MacroControlDefinition](../MacroControlDefinition/MacroControlDefinition.md)

## Description

Property that indicates the macro or filename associated with this MacroControlDefinition. A VBA macro must be a Public Sub defined in a standard code module of the Application VBA project. The Sub cannot have any input arguments. The Sub is specified using 'Module.SubName' format. For example, the Sub MovePart in a module named AsmTools would be specified by 'AsmTools.MovePart'. If a filename with an .ide extension is supplied it is assumed to be an iFeature. When the user clicks the button it will begin placement of the iFeature. The filename must be a full filename. If an external EXE is specified, this must be the full path to the EXE.

## Syntax

MacroControlDefinition.**MacroOrFileName**() As String

## Property Value

This is a read only property whose value is a String.

## Version

Introduced in version 9
