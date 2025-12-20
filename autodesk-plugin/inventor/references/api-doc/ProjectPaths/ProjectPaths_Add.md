# ProjectPaths.Add Method

Parent Object: [ProjectPaths](../ProjectPaths/ProjectPaths.md)

## Description

Method that adds a folder path after the target index and returns the newly created ProjectPath object.

## Syntax

ProjectPaths.**Add**( ***Name*** As String, ***Path*** As String, [***TargetIndex***] As Long ) As [ProjectPath](../ProjectPath/ProjectPath.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that specifies a display name for the path. |
| Path | String | Input String that specifies the folder path. |
| TargetIndex | Long | Optional input Long that specifies the position of the new path in the list. If not specified, the value defaults to 0 and the new path is added to the end of the list. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Query and create library paths](../../sample-programs/ProjectLibraryPaths_Sample.md) | The following sample demonstrates querying existing library paths associated with a project and adding a new library path. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |