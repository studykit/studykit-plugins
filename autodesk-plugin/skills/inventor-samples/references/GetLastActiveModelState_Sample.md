# Open assembly using last model state

## Description

This sample demonstrates how to open an assembly document in its last active model state.

## Code Samples

* [VBA](#VBA)

```
Public Sub OpenDocumentInLastActiveModelState()
    Dim strFullFileName As String
    strFullFileName = "C:\temp\Assembly1.iam"

    ' Set a reference to the FileManager object.
    Dim oFileManager As FileManager
    Set oFileManager = ThisApplication.FileManager

    ' Get the name of the last active model state.
    Dim strLastActiveMS As String
    strLastActiveMS = oFileManager.GetLastActiveModelState(strFullFileName)

    ' Use the full file name and ModelState name to get the full document name.
    Dim strFullDocumentName As String
    strFullDocumentName = oFileManager.GetFullDocumentName(strFullFileName, strLastActiveMS)

    ' Open the document in the last active model state.
    Dim oDoc As AssemblyDocument
    Set oDoc = ThisApplication.Documents.Open(strFullDocumentName)
End Sub
```
