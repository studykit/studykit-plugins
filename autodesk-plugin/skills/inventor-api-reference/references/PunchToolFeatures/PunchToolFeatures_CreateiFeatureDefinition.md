# PunchToolFeatures.CreateiFeatureDefinition Method

Parent Object: [PunchToolFeatures](../PunchToolFeatures/PunchToolFeatures.md)

## Description

Method that creates a new iFeatureDefinition.

## Remarks

The returned definition provides access to all of the inputs that are necessary for placing a punch feature. Using this object you provide the parameter and the geometry inputs necessary for placing the punch feature. Creating an iFeatureDefinition for use as input to create a punch tool feature (using the PunchToolFeatures.CreateiFeatureDefinition method results in an iFeatureDefinition that is slightly different than when created for a standard iFeature (using the iFeatures.CreateiFeatureDefinition method). For a punch tool iFeatureDefinition there is not a sketch plane input since the sketch plane is inferred by using the parent sketch of the input sketch points.

## Syntax

PunchToolFeatures.**CreateiFeatureDefinition**( ***FullFileName*** As String ) As [iFeatureDefinition](../iFeatureDefinition/iFeatureDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input string that specifies the name of the iFeature file (.ide) to create the definition for. The file must be an existing iFeature file. If an invalid file is specified an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |

## Version

Introduced in version 2009
