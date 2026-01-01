# DraftFeatureInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/DraftFeatureInput.h>

## Description

This class defines the methods and properties that pertain to the definition of a draft feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](DraftFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [setSingleAngle](DraftFeatureInput_setSingleAngle.htm) | Defines the draft to be defined so that a single angle is used for all drafts. If the isSymmetric is true then the faces are split along the parting plane and drafted independently using the same angle. |
| [setTwoAngles](DraftFeatureInput_setTwoAngles.htm) | Defines both angles to use when the surfaces are split along the draft plane and the faces on each side of the plane are drafted independently from the other side. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [angleOne](DraftFeatureInput_angleOne.htm) | Gets the first, or the only angle in the case of a single angle definition. |
| [angleTwo](DraftFeatureInput_angleTwo.htm) | Gets the second angle. This can be null in the case where a single angle definition is used. |
| [inputFaces](DraftFeatureInput_inputFaces.htm) | Gets and sets the input faces. If IsTangentChain is true, all the faces that are tangentially connected to the input faces (if any) will also be included. |
| [isDirectionFlipped](DraftFeatureInput_isDirectionFlipped.htm) | Gets and sets if the direction of the draft is flipped. |
| [isSymmetric](DraftFeatureInput_isSymmetric.htm) | Gets if the draft is symmetric from the draft plane. This only applies in the case where two angles have been specified and should be ignored otherwise. |
| [isTangentChain](DraftFeatureInput_isTangentChain.htm) | Gets and sets if any faces that are tangentially connected to any of the input faces will also be included in setting InputEntities. It defaults to true. |
| [isValid](DraftFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](DraftFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [plane](DraftFeatureInput_plane.htm) | Gets and sets the plane that defines the direction in which the draft is applied. This can be a planar BrepFace, or a ConstructionPlane. |
| [targetBaseFeature](DraftFeatureInput_targetBaseFeature.htm) | When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.   Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it. |

## Accessed From

[DraftFeatures.createInput](DraftFeatures_createInput.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Draft Feature API Sample](DraftFeatureSample_Sample.htm) | Demonstrates creating a new draft feature. |

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |