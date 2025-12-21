# iFeatureWorkPlaneInput Object

Derived from: [iFeatureInput](../iFeatureInput/iFeatureInput.md) Object

## Description

The iFeatureWorkPlaneInput object represents the work plane input information of an iFeature.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../iFeatureWorkPlaneInput/iFeatureWorkPlaneInput_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [EntityType](../iFeatureWorkPlaneInput/iFeatureWorkPlaneInput_EntityType.md) | Property that returns the type of geometry that are valid. The value returned is the sum of values specifying the valid entity types. |
| [FlipOption](../iFeatureWorkPlaneInput/iFeatureWorkPlaneInput_FlipOption.md) | Gets and sets whether direction of the selection needs to be flipped. |
| [Name](../iFeatureWorkPlaneInput/iFeatureWorkPlaneInput_Name.md) | Property that gets the name associated with this input. When placing an iFeature using the API you can use the name to identify each input when assigning the desired values and entities. |
| [PlaneInput](../iFeatureWorkPlaneInput/iFeatureWorkPlaneInput_PlaneInput.md) | Gets and sets the geometry matching the plane input. |
| [Prompt](../iFeatureWorkPlaneInput/iFeatureWorkPlaneInput_Prompt.md) | Property that gets the prompt that is used for this input during the placement of the iFeature. |
| [Type](../iFeatureWorkPlaneInput/iFeatureWorkPlaneInput_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |