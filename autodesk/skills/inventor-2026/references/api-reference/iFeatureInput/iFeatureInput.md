# iFeatureInput Object

## Description

The iFeatureInput object is the base class for iFeatureParameterInput, iFeatureEntityInput, iFeatureSketchPlaneInput, iFeatureWorkPlaneInput and iFeatureVectorInput.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatureInput/iFeatureInput_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [EntityType](../iFeatureInput/iFeatureInput_EntityType.md) | Property that returns the type of geometry that are valid. The value returned is the sum of values specifying the valid entity types. |
| [Name](../iFeatureInput/iFeatureInput_Name.md) | Property that gets the name associated with this input. When placing an iFeature using the API you can use the name to identify each input when assigning the desired values and entities. |
| [Prompt](../iFeatureInput/iFeatureInput_Prompt.md) | Property that gets the prompt that is used for this input during the placement of the iFeature. |
| [Type](../iFeatureInput/iFeatureInput_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[iFeatureInputs.Item](../iFeatureInputs/iFeatureInputs_Item.md)

## Derived Classes

[iFeatureEntityInput](../iFeatureEntityInput/iFeatureEntityInput.md), [iFeatureParameterInput](../iFeatureParameterInput/iFeatureParameterInput.md), [iFeatureSketchPlaneInput](../iFeatureSketchPlaneInput/iFeatureSketchPlaneInput.md), [iFeatureVectorInput](../iFeatureVectorInput/iFeatureVectorInput.md), [iFeatureWorkPlaneInput](../iFeatureWorkPlaneInput/iFeatureWorkPlaneInput.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Placement of a standard iFeature](../../sample-programs/iFeatures_Sample.md) | This program demonstrates the placement of a standard iFeature in a part. |
| [Place table driven iFeature](../../sample-programs/iFeatureTable_Sample.md) | This program demonstrates the placement of a table driven iFeature in a part. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |

## Version

Introduced in version 6
