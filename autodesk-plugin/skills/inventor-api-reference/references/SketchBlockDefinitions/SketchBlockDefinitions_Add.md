# SketchBlockDefinitions.Add Method

Parent Object: [SketchBlockDefinitions](../SketchBlockDefinitions/SketchBlockDefinitions.md)

## Description

Method that creates a new (empty) SketchBlockDefinition. The newly created SketchBlockDefinition is returned.

## Syntax

SketchBlockDefinitions.**Add**( [***Name***] As String, [***InsertionPoint***] As Variant ) As [SketchBlockDefinition](../SketchBlockDefinition/SketchBlockDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Optional input String that specifies a name for the sketch block definition. If not provided, the name is automatically generated. |
| InsertionPoint | Variant | Optional input Point2d object that specifies the insertion point for the sketch block. The insertion sketch point is created in space and no constraints are created on the insertion point. The insertion point can be retrieved using SketchBlockDefinition.InsertionPoint property and constraints can be added to it. If not specified, a default insertion point is chosen.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |