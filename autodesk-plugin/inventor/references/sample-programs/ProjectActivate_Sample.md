# Set active project

## Description

The following sample demonstrates the activation of an Inventor project.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub SetActiveProject()
    ' Check to make sure a document isn't open.
    If ThisApplication.Documents.Count > 0 Then
        MsgBox "All documents must be closed before changing the project."
        Exit Sub
    End If

    ' Set a reference to the DesignProjectManager object.
    Dim oDesignProjectMgr As DesignProjectManager
    Set oDesignProjectMgr = ThisApplication.DesignProjectManager

    ' Show the current project.
    Debug.Print "Old active project: " & oDesignProjectMgr.ActiveDesignProject.FullFileName

    ' Get the project to activate
    ' This assumes that "C:\Temp\MyProject.ipj" exists.
    Dim oProject As DesignProject
    Set oProject = oDesignProjectMgr.DesignProjects.ItemByName("C:\temp\MyProject.ipj")

    ' Activate the project
    oProject.Activate

    ' Show the current project after making the project change.
    Debug.Print "New active project: " & oDesignProjectMgr.ActiveDesignProject.FullFileName
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |