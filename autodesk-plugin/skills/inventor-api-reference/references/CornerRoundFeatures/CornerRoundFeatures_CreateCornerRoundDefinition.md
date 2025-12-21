# CornerRoundFeatures.CreateCornerRoundDefinition Method

Parent Object: [CornerRoundFeatures](../CornerRoundFeatures/CornerRoundFeatures.md)

## Description

Method that creates a new CornerRoundDefinition object.

## Remarks

This object is not a corner round feature but contains the information that defines a corner round feature and can be used to create a new corner round feature or edit an existing one. The returned CornerRoundDefinition can be used as input to the CornerRoundFeatures.Add method to create a new corner round feature. You can edit the properties of the CornerRoundDefinition object before creating the corner round feature to get the desired corner round feature.

## Syntax

CornerRoundFeatures.**CreateCornerRoundDefinition**( ***CornerEdges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md), ***Radius*** As Variant ) As [CornerRoundDefinition](../CornerRoundDefinition/CornerRoundDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CornerEdges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input EdgesCollection object that contains all of the corners to apply a corner round on. Any non-corner edges will be ignored. |
| Radius | Variant | Input Variant that defines the corner radius. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |