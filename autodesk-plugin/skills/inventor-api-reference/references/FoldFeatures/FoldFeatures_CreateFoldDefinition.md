# FoldFeatures.CreateFoldDefinition Method

Parent Object: [FoldFeatures](../FoldFeatures/FoldFeatures.md)

## Description

Method that creates a new FoldDefinition object.

## Remarks

This object is not a fold feature but contains the information that defines a fold feature and can be used to create a new fold feature or edit an existing one. The returned FoldDefinition can be used as input to the FoldFeatures.Add method to create a new fold feature. You can edit the properties of the FoldDefinition object before creating the fold feature to get the desired fold feature.

## Syntax

FoldFeatures.**CreateFoldDefinition**( ***BendLine*** As [SketchLine](../SketchLine/SketchLine.md), ***BendAngle*** As Variant ) As [FoldDefinition](../FoldDefinition/FoldDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BendLine | [SketchLine](../SketchLine/SketchLine.md) | Input SketchLine object that defines the location of the bend line. The bend line must be on the face you are folding, and must terminate at the edges of the face. |
| BendAngle | Variant | Input Variant that defines the bend angle. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |

## Version

Introduced in version 2011
