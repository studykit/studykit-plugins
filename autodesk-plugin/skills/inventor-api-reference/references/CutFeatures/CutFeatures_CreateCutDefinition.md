# CutFeatures.CreateCutDefinition Method

Parent Object: [CutFeatures](../CutFeatures/CutFeatures.md)

## Description

Method that creates a new CutDefinition object.

## Remarks

This object is not a cut feature but contains the information that defines a cut feature and can be used to create a new cut feature or edit an existing one. The returned CutDefinition can be used as input to the CutFeatures.Add method to create a new cut feature. You can edit the properties of the CutDefinition object before creating the cut feature to get the desired cut feature.

## Syntax

CutFeatures.**CreateCutDefinition**( ***Profile*** As [Profile](../Profile/Profile.md) ) As [CutDefinition](../CutDefinition/CutDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Profile | [Profile](../Profile/Profile.md) | Input Profile object that defines the shape of the cut feature. The input profile must consist of one or more closed paths. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |