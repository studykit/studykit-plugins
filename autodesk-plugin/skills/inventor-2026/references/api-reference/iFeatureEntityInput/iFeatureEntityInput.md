# iFeatureEntityInput Object

Derived from: [iFeatureInput](../iFeatureInput/iFeatureInput.md) Object

## Description

The iFeatureEntityInput object represents the positional information of an iFeature. The iFeatureEntityInput object is used both to describe and specify the geometry necessary for the placement of an iFeature.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatureEntityInput/iFeatureEntityInput_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Entity](../iFeatureEntityInput/iFeatureEntityInput_Entity.md) | Gets and sets the entity required for the input. |
| [EntityType](../iFeatureEntityInput/iFeatureEntityInput_EntityType.md) | Property that returns the type of geometry that are valid. The value returned is the sum of values specifying the valid entity types. |
| [Name](../iFeatureEntityInput/iFeatureEntityInput_Name.md) | Property that gets the name associated with this input. When placing an iFeature using the API you can use the name to identify each input when assigning the desired values and entities. |
| [Prompt](../iFeatureEntityInput/iFeatureEntityInput_Prompt.md) | Property that gets the prompt that is used for this input during the placement of the iFeature. |
| [Type](../iFeatureEntityInput/iFeatureEntityInput_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
