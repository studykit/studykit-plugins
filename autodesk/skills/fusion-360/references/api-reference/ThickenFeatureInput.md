# ThickenFeatureInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ThickenFeatureInput.h>

## Description

This class defines the methods and properties that pertain to the definition of a Thicken feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ThickenFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [creationOccurrence](ThickenFeatureInput_creationOccurrence.htm) | In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Thicken feature is created based on geometry (e.g. a profile and/or face(s)) in another component AND (the Thicken feature) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI |
| [inputFaces](ThickenFeatureInput_inputFaces.htm) | An ObjectCollection containing the face and/or patch bodies to thicken. |
| [isChainSelection](ThickenFeatureInput_isChainSelection.htm) | Get and sets whether faces that are tangentially connected to the input faces will be included in the thicken feature. |
| [isSymmetric](ThickenFeatureInput_isSymmetric.htm) | Gets and sets whether to add thickness symmetrically or only on one side of the face/s to thicken |
| [isValid](ThickenFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ThickenFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [operation](ThickenFeatureInput_operation.htm) | Gets and sets the feature operation to perform. |
| [targetBaseFeature](ThickenFeatureInput_targetBaseFeature.htm) | When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.   Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it. |
| [thickenType](ThickenFeatureInput_thickenType.htm) | The thicken type used when creating a thicken. The default value is SharpThickenType. |
| [thickness](ThickenFeatureInput_thickness.htm) | Gets and sets the ValueInput object that defines the thickness distance. |

## Accessed From

[ThickenFeatures.createInput](ThickenFeatures_createInput.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [thickenFeatures.add](thickenFeatures_add_Sample.htm) | Demonstrates the thickenFeatures.add method. |
| [Thicken Feature API Sample](ThickenFeatureSample_Sample.htm) | Demonstrates creating a new thiken feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |