# ExtentDefinition Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtentDefinition.h>

## Description

The base class for the various definition objects used to define the extent of a feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ExtentDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](ExtentDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ExtentDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentFeature](ExtentDefinition_parentFeature.htm) | Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null. |

## Accessed From

[DraftFeature.draftDefinition](DraftFeature_draftDefinition.htm), [ExtrudeFeature.extentOne](ExtrudeFeature_extentOne.htm), [ExtrudeFeature.extentTwo](ExtrudeFeature_extentTwo.htm), [ExtrudeFeature.startExtent](ExtrudeFeature_startExtent.htm), [ExtrudeFeatureInput.extentOne](ExtrudeFeatureInput_extentOne.htm), [ExtrudeFeatureInput.extentTwo](ExtrudeFeatureInput_extentTwo.htm), [ExtrudeFeatureInput.startExtent](ExtrudeFeatureInput_startExtent.htm), [HoleFeature.extentDefinition](HoleFeature_extentDefinition.htm), [RevolveFeature.extentDefinition](RevolveFeature_extentDefinition.htm)

## Derived Classes

[AllExtentDefinition](AllExtentDefinition.htm), [AngleExtentDefinition](AngleExtentDefinition.htm), [DistanceExtentDefinition](DistanceExtentDefinition.htm), [FromEntityStartDefinition](FromEntityStartDefinition.htm), [OffsetStartDefinition](OffsetStartDefinition.htm), [OneSideToExtentDefinition](OneSideToExtentDefinition.htm), [ProfilePlaneStartDefinition](ProfilePlaneStartDefinition.htm), [SymmetricExtentDefinition](SymmetricExtentDefinition.htm), [ThroughAllExtentDefinition](ThroughAllExtentDefinition.htm), [ToEntityExtentDefinition](ToEntityExtentDefinition.htm), [TwoSidesAngleExtentDefinition](TwoSidesAngleExtentDefinition.htm), [TwoSidesDistanceExtentDefinition](TwoSidesDistanceExtentDefinition.htm), [TwoSidesToExtentDefinition](TwoSidesToExtentDefinition.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |