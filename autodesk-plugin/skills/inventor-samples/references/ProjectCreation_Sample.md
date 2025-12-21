# Create project

## Description

The following sample demonstrates the creation of an Inventor project.

## Code Samples

* [VBA](#VBA)

|  |
| --- |
| Copy Code |

```
Public Sub CreateProject()
    ' Set a reference to the DesignProjectManager object.
    Dim oDesignProjectMgr As DesignProjectManager
    Set oDesignProjectMgr = ThisApplication.DesignProjectManager

    ' Create a new singler user project
    Dim oProject As DesignProject
    Set oProject = oDesignProjectMgr.DesignProjects.Add(kSingleUserMode, "MyProject", "C:\temp\")
End Sub
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |