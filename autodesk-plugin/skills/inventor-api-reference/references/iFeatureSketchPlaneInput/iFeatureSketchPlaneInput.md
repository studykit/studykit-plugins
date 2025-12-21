# iFeatureSketchPlaneInput Object

Derived from: [iFeatureInput](../iFeatureInput/iFeatureInput.md) Object

## Description

The iFeatureSketchPlaneInput object represents the sketch plane input information of an iFeature. The iFeatureSketchPlaneInput object is used specify the geometry's and other data necessary for the sketch plane input of an iFeature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [SetPosition](../iFeatureSketchPlaneInput/iFeatureSketchPlaneInput_SetPosition.md) | Method that sets the position of the iFeature on the plane provided. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatureSketchPlaneInput/iFeatureSketchPlaneInput_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [EntityType](../iFeatureSketchPlaneInput/iFeatureSketchPlaneInput_EntityType.md) | Property that returns the type of geometry that are valid. The value returned is the sum of values specifying the valid entity types. |
| [FlipOption](../iFeatureSketchPlaneInput/iFeatureSketchPlaneInput_FlipOption.md) | Gets and sets whether the geometry selection needs to be flipped. |
| [Name](../iFeatureSketchPlaneInput/iFeatureSketchPlaneInput_Name.md) | Property that gets the name associated with this input. When placing an iFeature using the API you can use the name to identify each input when assigning the desired values and entities. |
| [PlaneInput](../iFeatureSketchPlaneInput/iFeatureSketchPlaneInput_PlaneInput.md) | Gets and sets the geometry matching the sketch plane input. |
| [Prompt](../iFeatureSketchPlaneInput/iFeatureSketchPlaneInput_Prompt.md) | Property that gets the prompt that is used for this input during the placement of the iFeature. |
| [Type](../iFeatureSketchPlaneInput/iFeatureSketchPlaneInput_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Placement of a standard iFeature](../../sample-programs/iFeatures_Sample.md) | This program demonstrates the placement of a standard iFeature in a part. |

## Version

Introduced in version 6
