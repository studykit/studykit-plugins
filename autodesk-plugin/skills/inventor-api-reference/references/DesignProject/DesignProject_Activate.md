# DesignProject.Activate Method

Parent Object: [DesignProject](../DesignProject/DesignProject.md)

## Description

Method that activates the DesignProject. This requires all the documents to be closed in Inventor.

## Syntax

DesignProject.**Activate**( [***SetAsDefaultProject***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SetAsDefaultProject | Boolean | Optional input Boolean that specifies whether this project should be set as the default project for the next session of Inventor and Apprentice. If not specified, a value of True is used indicating the this project will be set as the default. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Set active project](../../sample-programs/ProjectActivate_Sample.md) | The following sample demonstrates the activation of an Inventor project. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |