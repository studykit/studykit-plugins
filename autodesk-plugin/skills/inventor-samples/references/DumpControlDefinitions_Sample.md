# Print list of all Inventor Commands

## Description

This sample prints the internal names and descriptions of all commands (aka ControlDefinitions) in Inventor.

## Code Samples

* [VBA](#VBA)

The sample prints the names and descriptions to a text file (CommandNames.txt) created in C:\Temp directory. You should either have the C:\Temp directory or change the path in the sample.

```
Sub PrintCommandNames()
    Dim oControlDefs As ControlDefinitions
    Set oControlDefs = ThisApplication.CommandManager.ControlDefinitions

    Dim oControlDef As ControlDefinition

    Open "C:\temp\CommandNames.txt" For Output As #1

    Print #1, Tab(10); "Command Name"; Tab(75); "Description"; vbNewLine

    For Each oControlDef In oControlDefs

        Print #1, oControlDef.InternalName; Tab(55); oControlDef.DescriptionText

    Next
    Close #1
End Sub
```
