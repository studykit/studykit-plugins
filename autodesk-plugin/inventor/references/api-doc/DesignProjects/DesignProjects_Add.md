# DesignProjects.Add Method

Parent Object: [DesignProjects](../DesignProjects/DesignProjects.md)

## Description

Method that creates a new DesignProject. The newly created DesignProject is returned.

## Syntax

DesignProjects.**Add**( ***ProjectType*** As [MultiUserModeEnum](../MultiUserModeEnum.md), ***Name*** As String, ***ProjectPath*** As String ) As [DesignProject](../DesignProject/DesignProject.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ProjectType | [MultiUserModeEnum](../MultiUserModeEnum.md) | Input MultiUserModeEnum that specifies the type of project to create. |
| Name | String | Input String that specifies a name for the project. |
| ProjectPath | String | Input String that specifies the project (workspace or workgroup) folder for the project. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create project](../../sample-programs/ProjectCreation_Sample.md) | The following sample demonstrates the creation of an Inventor project. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |