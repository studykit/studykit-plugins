# OffsetFeatureInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/OffsetFeatureInput.h>

## Description

This class defines the methods and properties that pertain to the definition of an offset feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](OffsetFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [distance](OffsetFeatureInput_distance.htm) | Gets and sets the ValueInput object that defines the offset distance. A positive distance value results in an offset in the positive normal direction of the faces. |
| [entities](OffsetFeatureInput_entities.htm) | An ObjectCollection containing the BRepFace objects being offset. |
| [isChainSelection](OffsetFeatureInput_isChainSelection.htm) | Get and sets whether faces that are tangentially connected to the input faces will be included in the offset. |
| [isValid](OffsetFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](OffsetFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [operation](OffsetFeatureInput_operation.htm) | Gets and sets the feature operation to perform. Can be 'NewBodyFeatureOperation' or 'NewComponentFeatureOperation'. |
| [targetBaseFeature](OffsetFeatureInput_targetBaseFeature.htm) | When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.   Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it. |

## Accessed From

[OffsetFeatures.createInput](OffsetFeatures_createInput.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Offset Feature API Sample](OffsetFeatureSample_Sample.htm) | Demonstrates creating a new offset feature |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |