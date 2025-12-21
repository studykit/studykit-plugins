# Query and create library paths

## Description

The following sample demonstrates querying existing library paths associated with a project and adding a new library path.

## Code Samples

* [VBA](#VBA)

```
Sub QueryAndCreateLibraryPaths()
    Dim oProjectMgr As DesignProjectManager
    Set oProjectMgr = ThisApplication.DesignProjectManager

    ' Get the active project
    Dim oProject As DesignProject
    Set oProject = oProjectMgr.ActiveDesignProject

    Dim oLibraryPaths As ProjectPaths
    Set oLibraryPaths = oProject.LibraryPaths

    ' Add a new library path to the end of the list
    Call oLibraryPaths.Add("MyLibraryPath", "C:\temp\MyLibrary")

    ' Print all library names and paths
    Dim oLibraryPath As ProjectPath
    For Each oLibraryPath In oLibraryPaths
        Debug.Print "Name: " & oLibraryPath.Name & " Path: " & oLibraryPath.Path
    Next
End Sub
```
