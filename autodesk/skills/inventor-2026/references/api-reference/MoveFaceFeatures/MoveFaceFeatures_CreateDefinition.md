# MoveFaceFeatures.CreateDefinition Method

Parent Object: [MoveFaceFeatures](../MoveFaceFeatures/MoveFaceFeatures.md)

## Description

Method that creates a new MoveFaceDefinition object

## Remarks

The object created does not represent a move face feature but instead is a representation of the information that defines a move face feature. You can use this object as input to the MoveFaceFeatures.Add method to create the actual feature. The MoveFaceDefinition object returned is fully defined and can be used to create a move face feature. However, defaults are used for move face options, so you may want to change some of the property values of the MoveFaceDefinition object before using it to create a feature.

## Syntax

MoveFaceFeatures.**CreateDefinition**( ***Faces*** As [FaceCollection](../FaceCollection/FaceCollection.md) ) As [MoveFaceDefinition](../MoveFaceDefinition/MoveFaceDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Faces | [FaceCollection](../FaceCollection/FaceCollection.md) | FaceCollection object that specifies the faces to move. |

## Version

Introduced in version 2011
